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
    var stage = lb.querySelector('.lightbox-stage');
    var lbImg = lb.querySelector('#lightbox-img-main');
    var btnClose = lb.querySelector('.lightbox-close');
    var btnPrev = lb.querySelector('.lightbox-prev');
    var btnNext = lb.querySelector('.lightbox-next');
    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var current = 0;
    var sliding = false;

    function infoFor(index) {
      var trigger = items[index];
      var innerImg = trigger.querySelector('img');
      var src = trigger.getAttribute('href') || (innerImg && innerImg.src) || '';
      var alt = (innerImg && innerImg.alt) || trigger.getAttribute('data-alt') || trigger.textContent.trim();
      return { src: src, alt: alt };
    }

    function show(index) {
      current = (index + items.length) % items.length;
      var info = infoFor(current);
      lbImg.src = info.src;
      lbImg.alt = info.alt;
    }

    function navigate(delta) {
      if (sliding || items.length < 2) {
        show(current + delta);
        return;
      }
      var dir = delta > 0 ? 1 : -1;
      var nextIndex = (current + delta + items.length) % items.length;
      var info = infoFor(nextIndex);

      if (reduceMotion || !stage) {
        current = nextIndex;
        lbImg.src = info.src;
        lbImg.alt = info.alt;
        return;
      }

      sliding = true;
      var clone = lbImg.cloneNode(true);
      clone.removeAttribute('id');
      clone.classList.add('lightbox-img-clone');
      clone.setAttribute('aria-hidden', 'true');
      clone.style.transition = 'none';
      clone.style.transform = 'translate(-50%, -50%) translateX(0)';
      stage.appendChild(clone);

      current = nextIndex;
      lbImg.src = info.src;
      lbImg.alt = info.alt;
      lbImg.style.transition = 'none';
      lbImg.style.transform = 'translateX(' + (dir * 100) + '%)';
      void lbImg.offsetWidth;

      requestAnimationFrame(function () {
        clone.style.transition = 'transform .38s ease';
        clone.style.transform = 'translate(-50%, -50%) translateX(' + (dir * -100) + '%)';
        lbImg.style.transition = 'transform .38s ease';
        lbImg.style.transform = 'translateX(0)';
      });

      lbImg.addEventListener('transitionend', function onEnd() {
        lbImg.removeEventListener('transitionend', onEnd);
        clone.remove();
        lbImg.style.transition = '';
        lbImg.style.transform = '';
        sliding = false;
      }, { once: true });
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
    btnPrev.addEventListener('click', function () { navigate(-1); });
    btnNext.addEventListener('click', function () { navigate(1); });
    lb.addEventListener('click', function (e) {
      if (e.target === lb) close();
    });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') navigate(-1);
      if (e.key === 'ArrowRight') navigate(1);
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    initImageFade();
    initCarousels();
    initEquipPanels();
    initLightbox();
  });
})();
