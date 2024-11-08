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
    let ticking = false;
    window.addEventListener('scroll', function() {
        if (!ticking) {
            window.requestAnimationFrame(function() {
                document.body.classList.toggle('fixedHeader', window.scrollY > 10);
                ticking = false;
            });
            ticking = true;
        }
    });

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