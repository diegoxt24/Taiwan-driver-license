const CACHE_NAME = 'tw-driving-prep-v2';
const ASSETS = [
  './',
  './index.html',
  './styles.css',
  './app.js',
  './questions.json',
  './car_questions.json',
  './cheat_sheet.json',
  './car_cheat_sheet.json',
  './moto_master_rules.json',
  './car_master_rules.json',
  './manifest.json'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
  );
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request).then((res) => res || fetch(e.request))
  );
});
