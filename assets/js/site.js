(function () {
  'use strict';

  function initCarousels() {
    document.querySelectorAll('.carousel').forEach(function (carousel) {
      var track = carousel.querySelector('.h-scroll');
      var prev = carousel.querySelector('.carousel-arrow.prev');
      var next = carousel.querySelector('.carousel-arrow.next');
      if (!track || !prev || !next) return;

      function step() {
        var item = track.querySelector(':scope > *');
        var gap = parseFloat(getComputedStyle(track).columnGap || 24) || 24;
        var itemWidth = item ? item.getBoundingClientRect().width : track.clientWidth * 0.8;
        return itemWidth + gap;
      }

      function updateArrows() {
        var max = track.scrollWidth - track.clientWidth - 2;
        prev.classList.toggle('disabled', track.scrollLeft <= 2);
        next.classList.toggle('disabled', track.scrollLeft >= max);
      }

      prev.addEventListener('click', function () {
        track.scrollBy({ left: -step(), behavior: 'smooth' });
      });
      next.addEventListener('click', function () {
        track.scrollBy({ left: step(), behavior: 'smooth' });
      });
      track.addEventListener('scroll', updateArrows, { passive: true });
      window.addEventListener('resize', updateArrows);
      updateArrows();
    });
  }

  function initLightbox() {
    var items = [].slice.call(document.querySelectorAll('.lightbox-trigger'));
    if (!items.length) return;

    var lb = document.getElementById('lightbox');
    if (!lb) return;
    var lbImg = lb.querySelector('.lightbox-img');
    var btnClose = lb.querySelector('.lightbox-close');
    var btnPrev = lb.querySelector('.lightbox-prev');
    var btnNext = lb.querySelector('.lightbox-next');
    var current = 0;

    function show(index) {
      current = (index + items.length) % items.length;
      var src = items[current].getAttribute('href') || items[current].querySelector('img').src;
      var alt = items[current].querySelector('img').alt || '';
      lbImg.src = src;
      lbImg.alt = alt;
    }

    function open(index) {
      show(index);
      lb.classList.add('open');
      document.body.style.overflow = 'hidden';
    }

    function close() {
      lb.classList.remove('open');
      document.body.style.overflow = '';
    }

    items.forEach(function (el, i) {
      el.addEventListener('click', function (e) {
        e.preventDefault();
        open(i);
      });
    });

    btnClose.addEventListener('click', close);
    btnPrev.addEventListener('click', function () { show(current - 1); });
    btnNext.addEventListener('click', function () { show(current + 1); });
    lb.addEventListener('click', function (e) {
      if (e.target === lb) close();
    });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(current - 1);
      if (e.key === 'ArrowRight') show(current + 1);
    });
  }

  function initServicesNavState() {
    var links = document.querySelectorAll('.nav-links a[href$="#services"]');
    if (!links.length) return;

    function update() {
      var isServices = window.location.hash === '#services';
      links.forEach(function (a) {
        a.classList.toggle('active', isServices);
      });
    }

    update();
    window.addEventListener('hashchange', update);
  }

  document.addEventListener('DOMContentLoaded', function () {
    initCarousels();
    initLightbox();
    initServicesNavState();
  });
})();
