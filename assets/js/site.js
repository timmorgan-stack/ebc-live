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

  function initImageFade() {
    function revealOnLoad(img) {
      if (img.complete && img.naturalWidth) {
        img.classList.add('is-loaded');
        return;
      }
      function onDone() {
        img.classList.add('is-loaded');
        img.removeEventListener('load', onDone);
        img.removeEventListener('error', onDone);
      }
      img.addEventListener('load', onDone);
      img.addEventListener('error', onDone);
    }

    var all = [].slice.call(document.querySelectorAll('img'));
    // Chrome/nav furniture fades in as soon as it's ready — it's already
    // on screen, so there's nothing to wait to scroll to.
    var immediate = all.filter(function (img) {
      return img.classList.contains('hero-bg') ||
        img.classList.contains('footer-logo') ||
        img.classList.contains('lightbox-img') ||
        !!img.closest('.nav-logo');
    });
    var content = all.filter(function (img) { return immediate.indexOf(img) === -1; });

    immediate.forEach(revealOnLoad);

    if (!('IntersectionObserver' in window)) {
      content.forEach(revealOnLoad);
      return;
    }

    var observer = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        revealOnLoad(entry.target);
        obs.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.1 });

    content.forEach(function (img) { observer.observe(img); });
  }

  function initEquipPanels() {
    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    document.querySelectorAll('.equip-cat').forEach(function (details) {
      var summary = details.querySelector(':scope > summary');
      var content = details.querySelector(':scope > ul');
      if (!summary || !content || reduceMotion || !details.animate) return;

      var animation = null;
      var closing = false;
      var expanding = false;

      function onFinish(open) {
        details.open = open;
        animation = null;
        closing = false;
        expanding = false;
        details.style.height = '';
        details.style.overflow = '';
      }

      function expand() {
        details.style.overflow = 'hidden';
        expanding = true;
        var startHeight = details.offsetHeight + 'px';
        details.open = true;
        var endHeight = (summary.offsetHeight + content.offsetHeight) + 'px';
        if (animation) animation.cancel();
        animation = details.animate(
          { height: [startHeight, endHeight] },
          { duration: 220, easing: 'ease' }
        );
        animation.onfinish = function () { onFinish(true); };
        animation.oncancel = function () { expanding = false; };
      }

      function collapse() {
        details.style.overflow = 'hidden';
        closing = true;
        var startHeight = details.offsetHeight + 'px';
        var endHeight = summary.offsetHeight + 'px';
        if (animation) animation.cancel();
        animation = details.animate(
          { height: [startHeight, endHeight] },
          { duration: 180, easing: 'ease' }
        );
        animation.onfinish = function () { onFinish(false); };
        animation.oncancel = function () { closing = false; };
      }

      summary.addEventListener('click', function (e) {
        e.preventDefault();
        if (closing || !details.open) {
          expand();
        } else if (expanding || details.open) {
          collapse();
        }
      });
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
      var trigger = items[current];
      var innerImg = trigger.querySelector('img');
      var src = trigger.getAttribute('href') || (innerImg && innerImg.src) || '';
      var alt = (innerImg && innerImg.alt) || trigger.getAttribute('data-alt') || trigger.textContent.trim();
      lbImg.src = src;
      lbImg.alt = alt;
    }

    function open(index) {
      show(index);
      var multi = items.length > 1;
      btnPrev.style.display = multi ? '' : 'none';
      btnNext.style.display = multi ? '' : 'none';
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

  document.addEventListener('DOMContentLoaded', function () {
    initImageFade();
    initCarousels();
    initEquipPanels();
    initLightbox();
  });
})();
