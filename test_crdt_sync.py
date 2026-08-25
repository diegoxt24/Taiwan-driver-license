import json
import unittest

def merge_cloud_and_local_state(remote_data, local_data):
    if not remote_data or not isinstance(remote_data, dict):
        return local_data or {}
    if not local_data or not isinstance(local_data, dict):
        local_data = {}

    profiles = ['diego', 'johana', 'alejandro']
    modules = ['motorcycle', 'car']
    tab_keys = ['sheppard1', 'sheppard2', 'interactive', 'mode0', 'bookmarks', 'failed']

    remote_is_newer = (int(remote_data.get('last_updated', 0) or 0)) > (int(local_data.get('last_updated', 0) or 0))

    for prof in profiles:
        if prof not in local_data:
            local_data[prof] = {}
        r_prof = remote_data.get(prof)
        l_prof = local_data[prof]

        if r_prof:
            if r_prof.get('name') and not l_prof.get('name'):
                l_prof['name'] = r_prof['name']

            for mod in modules:
                if mod not in l_prof:
                    l_prof[mod] = {
                        'bookmarks': [],
                        'failedQuestions': [],
                        'studiedQuestions': [],
                        'examHistory': [],
                        'lastIndices': {'sheppard1': 0, 'sheppard2': 0, 'interactive': 0, 'mode0': 0, 'bookmarks': 0, 'failed': 0}
                    }
                if 'lastIndices' not in l_prof[mod]:
                    l_prof[mod]['lastIndices'] = {'sheppard1': 0, 'sheppard2': 0, 'interactive': 0, 'mode0': 0, 'bookmarks': 0, 'failed': 0}

                r_mod = r_prof.get(mod)
                if r_mod:
                    # 1. Non-destructive Set-Union for Studied Questions
                    r_studied = r_mod.get('studiedQuestions', []) if isinstance(r_mod.get('studiedQuestions'), list) else []
                    l_studied = l_prof[mod].get('studiedQuestions', []) if isinstance(l_prof[mod].get('studiedQuestions'), list) else []
                    l_prof[mod]['studiedQuestions'] = list(dict.fromkeys(l_studied + r_studied))

                    # 2. Failed Questions: If remote is newer, adopt remote failed list so clears/resets propagate
                    if remote_is_newer:
                        l_prof[mod]['failedQuestions'] = list(r_mod.get('failedQuestions', [])) if isinstance(r_mod.get('failedQuestions'), list) else []
                    else:
                        l_prof[mod]['failedQuestions'] = list(l_prof[mod].get('failedQuestions', [])) if isinstance(l_prof[mod].get('failedQuestions'), list) else []

                    # 3. Non-destructive Set-Union for Bookmarks
                    r_book = r_mod.get('bookmarks', []) if isinstance(r_mod.get('bookmarks'), list) else []
                    l_book = l_prof[mod].get('bookmarks', []) if isinstance(l_prof[mod].get('bookmarks'), list) else []
                    l_prof[mod]['bookmarks'] = list(dict.fromkeys(l_book + r_book))

                    # 4. Exam History Union (keyed by date)
                    r_exams = r_mod.get('examHistory', []) if isinstance(r_mod.get('examHistory'), list) else []
                    l_exams = l_prof[mod].get('examHistory', []) if isinstance(l_prof[mod].get('examHistory'), list) else []
                    exam_map = {ex['date']: ex for ex in (l_exams + r_exams) if isinstance(ex, dict) and 'date' in ex}
                    l_prof[mod]['examHistory'] = list(exam_map.values())

                    # 5. Smart Index Resolution: Only adopt remote indices if remote state is strictly newer
                    if remote_is_newer and isinstance(r_mod.get('lastIndices'), dict):
                        for tk in tab_keys:
                            if tk in r_mod['lastIndices']:
                                l_prof[mod]['lastIndices'][tk] = int(r_mod['lastIndices'][tk])

    local_data['last_updated'] = max(
        int(local_data.get('last_updated', 0) or 0),
        int(remote_data.get('last_updated', 0) or 0)
    )
    return local_data


class TestSyncEngineCRDT(unittest.TestCase):

    def test_offline_flight_and_landing_union(self):
        # Initial cloud state before flight
        cloud_state = {
            'diego': {
                'car': {
                    'studiedQuestions': ['CAR_0001', 'CAR_0002'],
                    'bookmarks': ['CAR_0046'],
                    'failedQuestions': [],
                    'lastIndices': {'sheppard1': 2, 'mode0': 0}
                }
            },
            'last_updated': 1000
        }

        # Pilot boards flight, airplane mode ON, studies 5 new questions offline on iPad
        ipad_local_state = json.loads(json.dumps(cloud_state))
        ipad_local_state['diego']['car']['studiedQuestions'].extend(['CAR_0003', 'CAR_0004', 'CAR_0005'])
        ipad_local_state['diego']['car']['bookmarks'].append('CAR_0058')
        ipad_local_state['diego']['car']['lastIndices']['sheppard1'] = 5
        ipad_local_state['last_updated'] = 2000

        # Meanwhile, spouse Johana studies car on PC at home
        cloud_state['johana'] = {
            'car': {
                'studiedQuestions': ['CAR_0100', 'CAR_0101'],
                'bookmarks': ['CAR_0100'],
                'failedQuestions': ['CAR_0102'],
                'lastIndices': {'sheppard1': 2}
            }
        }
        cloud_state['last_updated'] = 1500

        # iPad lands, connects to airport Wi-Fi -> triggers auto-sync merge
        merged = merge_cloud_and_local_state(cloud_state, ipad_local_state)

        # Assert Diego's offline progress was NOT lost
        self.assertEqual(len(merged['diego']['car']['studiedQuestions']), 5)
        self.assertIn('CAR_0005', merged['diego']['car']['studiedQuestions'])
        self.assertIn('CAR_0058', merged['diego']['car']['bookmarks'])
        self.assertEqual(merged['diego']['car']['lastIndices']['sheppard1'], 5)

        # Assert Johana's progress from cloud was also merged cleanly
        self.assertIn('johana', merged)
        self.assertEqual(len(merged['johana']['car']['studiedQuestions']), 2)
        self.assertIn('CAR_0100', merged['johana']['car']['studiedQuestions'])

    def test_smart_timestamp_last_indices(self):
        # Device A has last_updated 2000 (newer) and reached question 120 in Sheppard1
        # Device B has last_updated 1000 (older) and reached question 45
        local_a = {
            'diego': {
                'car': {
                    'studiedQuestions': ['CAR_0001'],
                    'lastIndices': {'sheppard1': 120, 'mode0': 10}
                }
            },
            'last_updated': 2000
        }
        cloud_b = {
            'diego': {
                'car': {
                    'studiedQuestions': ['CAR_0002'],
                    'lastIndices': {'sheppard1': 45, 'mode0': 25}
                }
            },
            'last_updated': 1000
        }
        merged = merge_cloud_and_local_state(cloud_b, local_a)
        # Because local_a is newer, its indices 120 and 10 are preserved
        self.assertEqual(merged['diego']['car']['lastIndices']['sheppard1'], 120)
        self.assertEqual(merged['diego']['car']['lastIndices']['mode0'], 10)
        # Studied questions should be non-destructive union: ['CAR_0001', 'CAR_0002']
        self.assertEqual(set(merged['diego']['car']['studiedQuestions']), {'CAR_0001', 'CAR_0002'})

    def test_malformed_and_empty_cloud_payload(self):
        local = {
            'diego': {
                'car': {
                    'studiedQuestions': ['CAR_0001'],
                    'bookmarks': ['CAR_0046'],
                    'lastIndices': {'sheppard1': 1}
                }
            }
        }
        # Null remote
        res1 = merge_cloud_and_local_state(None, json.loads(json.dumps(local)))
        self.assertEqual(res1['diego']['car']['studiedQuestions'], ['CAR_0001'])

        # Empty dict remote
        res2 = merge_cloud_and_local_state({}, json.loads(json.dumps(local)))
        self.assertEqual(res2['diego']['car']['studiedQuestions'], ['CAR_0001'])

        # Corrupted non-list fields in remote
        corrupted_remote = {
            'diego': {
                'car': {
                    'studiedQuestions': 'NOT_A_LIST',
                    'bookmarks': None,
                    'lastIndices': 'INVALID'
                }
            }
        }
        res3 = merge_cloud_and_local_state(corrupted_remote, json.loads(json.dumps(local)))
        self.assertEqual(res3['diego']['car']['studiedQuestions'], ['CAR_0001'])
        self.assertEqual(res3['diego']['car']['bookmarks'], ['CAR_0046'])

if __name__ == '__main__':
    unittest.main()
