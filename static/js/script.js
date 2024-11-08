// DOMの読み込みを待つ
document.addEventListener('DOMContentLoaded', function() {
    // ナビゲーションの切り替え - 必要な場合のみ初期化
    const navToggle = document.querySelector('.navToggle');
    if (navToggle) {
        navToggle.addEventListener('click', function(e) {
            e.preventDefault();
            document.body.classList.toggle('navToggleActive');
        });
    }

    // スクロールヘッダー - スロットリング適用
    let lastScrollTop = 0;
    let ticking = false;
    
    window.addEventListener('scroll', function() {
        if (!ticking) {
            window.requestAnimationFrame(function() {
                const currentScroll = window.pageYOffset || document.documentElement.scrollTop;
                
                // スクロール方向を検出
                if (currentScroll > lastScrollTop) {
                    // 下スクロール
                    document.body.classList.remove('scrollUp');
                    document.body.classList.add('scrollDown');
                } else {
                    // 上スクロール
                    document.body.classList.remove('scrollDown');
                    document.body.classList.add('scrollUp');
                }

                // 固定ヘッダーの制御
                document.body.classList.toggle('fixedHeader', currentScroll > 10);
                
                lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
                ticking = false;
            });
            ticking = true;
        }
    }, { passive: true });

    // Swiperの初期化 - 要素が存在する場合のみ初期化
    const testimonialElement = document.querySelector('.testimonialSwiper');
    if (testimonialElement) {
        new Swiper(testimonialElement, {
            navigation: {
                nextEl: '.test-swiper-button-next',
                prevEl: '.test-swiper-button-prev',
            }
        });
    }

    const certificatesElement = document.querySelector('.certificatesSlider');
    if (certificatesElement) {
        new Swiper(certificatesElement, {
            slidesPerView: 1,
            spaceBetween: 16,
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.cert-swiper-button-next',
                prevEl: '.cert-swiper-button-prev',
            },
            breakpoints: {
                640: {
                    slidesPerView: 2,
                    spaceBetween: 16,
                },
                768: {
                    slidesPerView: 2,
                    spaceBetween: 16,
                },
                1024: {
                    slidesPerView: 2,
                    spaceBetween: 16,
                }
            }
        });
    }
});