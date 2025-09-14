import streamlit as st
import streamlit.components.v1 as components

def render_page_header():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600&display=swap');

    html {
        scroll-behavior: smooth;
    }

    .stDeployButton {
        display: none !important;
    }

    .stDecoration {
        display: none !important;
    }

    .stStatusWidget {
        display: none !important;
    }

    .stProgress {
        display: none !important;
    }

    .stException {
        display: none !important;
    }


    .section-anchor {
        scroll-margin-top: 20px;
    }

    .header-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        height: 45px;
        margin: 0 auto;
        font-family: 'Montserrat', sans-serif !important;
        position: relative;
    }

    a {
        text-decoration: none;
        color: inherit;
    }
    .st-emotion-cache-1jx6334 a {
        all: unset;
        color: inherit;
        text-decoration: none;
    }

    .logo-section {
        display: flex;
        align-items: center;
        gap: 1rem;
        z-index: 1001;
    }

    .nav-section {
        display: flex;
        gap: 2rem;
        align-items: center;
    }

    .nav-link {
        color: white !important;
        text-decoration: none;
        cursor:pointer !important;
        font-weight: 500;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        transition: color 0.3s ease;
    }

    .nav-link:hover {
        color: #6D4BC4 !important;
    }

    .outline-button {
        padding: 11px 17px;
        border: 1px solid transparent;
        background:
          linear-gradient(#0A0A0A, #0A0A0A) padding-box,
          linear-gradient(90deg, #9588D4 47%, #4D476E 100%) border-box;
        -webkit-background-clip: padding-box, border-box;
        background-clip: padding-box, border-box;
        -webkit-text-fill-color: initial;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .outline-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(109, 75, 196, 0.3);
    }

    /* Hamburger Menu */
    .hamburger {
        display: none;
        flex-direction: column;
        cursor: pointer;
        padding: 4px;
        z-index: 1001;
    }

    .hamburger span {
        width: 25px;
        height: 3px;
        background-color: white;
        margin: 3px 0;
        transition: 0.3s;
        border-radius: 2px;
    }

    .hamburger.active span:nth-child(1) {
        transform: rotate(-45deg) translate(-5px, 6px);
    }

    .hamburger.active span:nth-child(2) {
        opacity: 0;
    }

    .hamburger.active span:nth-child(3) {
        transform: rotate(45deg) translate(-5px, -6px);
    }

    .mobile-menu {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100vh;
        background: rgba(10, 10, 10, 0.98);
        backdrop-filter: blur(15px);
        z-index: 1000;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 0;
        opacity: 0;
        visibility: hidden;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        transform: translateY(-20px);
    }

    .mobile-menu.active {
        opacity: 1;
        visibility: visible;
        transform: translateY(0);
    }

    .hamburger-checkbox {
        display: none;
    }

    .hamburger-label {
        display: none;
        flex-direction: column;
        cursor: pointer;
        padding: 4px;
        z-index: 1001;
    }

    .hamburger-label span {
        width: 25px;
        height: 3px;
        background-color: white;
        margin: 3px 0;
        transition: 0.3s;
        border-radius: 2px;
    }

    .hamburger-checkbox:checked ~ .mobile-menu {
        opacity: 1;
        visibility: visible;
        transform: translateY(0);
    }

    .hamburger-checkbox:checked ~ .hamburger-label span:nth-child(1) {
        transform: rotate(-45deg) translate(-5px, 6px);
    }

    .hamburger-checkbox:checked ~ .hamburger-label span:nth-child(2) {
        opacity: 0;
    }

    .hamburger-checkbox:checked ~ .hamburger-label span:nth-child(3) {
        transform: rotate(45deg) translate(-5px, -6px);
    }

    /* Мобильные ссылки теперь являются label для checkbox - автоматически закрывают меню */

    .mobile-nav-link {
        color: white !important;
        text-decoration: none;
        font-weight: 500;
        font-size: 1.8rem;
        padding: 1.5rem 3rem;
        border-radius: 15px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        text-align: center;
        position: relative;
        overflow: hidden;
        margin: 0.5rem 0;
        min-width: 250px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
    }

    .mobile-nav-link a {
        color: white !important;
        text-decoration: none;
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .mobile-nav-link::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(109, 75, 196, 0.2), transparent);
        transition: left 0.5s;
    }

    .mobile-nav-link:hover::before {
        left: 100%;
    }

    .mobile-nav-link:hover {
        color: #6D4BC4 !important;
        background: rgba(109, 75, 196, 0.15);
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 8px 25px rgba(109, 75, 196, 0.3);
    }

    .mobile-button {
        margin-top: 2rem;
        padding: 18px 40px;
        font-size: 1.2rem;
        border-radius: 15px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        min-width: 250px;
    }

    .mobile-button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 10px 30px rgba(109, 75, 196, 0.4);
    }


    @media (max-width: 768px) {
        .nav-section, .learn-more {
            display: none;
        }

        .hamburger-label {
            display: flex;
        }

        .mobile-menu {
            display: flex;
        }

        .header-content {
            padding: 0 1rem;
        }
    }

    @media (max-width: 480px) {
        .logo-section svg {
            width: 80px;
            height: 20px;
        }

        .mobile-nav-link {
            font-size: 1.2rem;
            padding: 0.8rem 1.5rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="header-content">
            <div class="logo-section">
                <svg width="114" height="26" viewBox="0 0 114 26" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M20.2204 17.9457H15.406H14.9934V6.5C14.9934 5.93478 14.0763 5.32246 13.6178 5.08696H4.81438V19.5293L0 16.6739V0H13.8929C18.1846 0 19.8995 4.33333 20.2204 6.5V17.9457Z" fill="#6D4BC4"/>
                <path d="M23 26L20.0616 20.7717H14.3056C13.2052 20.7717 12.655 19.5471 12.5174 18.9348V7.77174H7.56546V20.4891C8.27312 23.2022 11.4367 25.2935 12.9301 26H23Z" fill="#6D4BC4"/>
                <path d="M27.762 20L33.015 8.1H36.33L41.6 20H38.098L33.984 9.749H35.31L31.196 20H27.762ZM30.635 17.688L31.502 15.206H37.316L38.183 17.688H30.635ZM46.2623 20.153C45.4349 20.153 44.6756 19.9603 43.9843 19.575C43.2929 19.1897 42.7433 18.64 42.3353 17.926C41.9386 17.212 41.7403 16.3677 41.7403 15.393C41.7403 14.4183 41.9386 13.5797 42.3353 12.877C42.7433 12.163 43.2929 11.6133 43.9843 11.228C44.6756 10.8313 45.4349 10.633 46.2623 10.633C47.1009 10.633 47.7923 10.803 48.3363 11.143C48.8803 11.483 49.2883 12.0043 49.5603 12.707C49.8323 13.3983 49.9683 14.2937 49.9683 15.393C49.9683 16.481 49.8209 17.3763 49.5263 18.079C49.2429 18.7703 48.8236 19.2917 48.2683 19.643C47.7243 19.983 47.0556 20.153 46.2623 20.153ZM46.9423 17.586C47.3049 17.586 47.6279 17.501 47.9113 17.331C48.2059 17.161 48.4383 16.9117 48.6083 16.583C48.7896 16.2543 48.8803 15.8577 48.8803 15.393C48.8803 14.9283 48.7896 14.5317 48.6083 14.203C48.4383 13.8743 48.2059 13.625 47.9113 13.455C47.6279 13.285 47.3049 13.2 46.9423 13.2C46.5796 13.2 46.2509 13.285 45.9563 13.455C45.6729 13.625 45.4406 13.8743 45.2593 14.203C45.0893 14.5317 45.0043 14.9283 45.0043 15.393C45.0043 15.8577 45.0893 16.2543 45.2593 16.583C45.4406 16.9117 45.6729 17.161 45.9563 17.331C46.2509 17.501 46.5796 17.586 46.9423 17.586ZM48.8293 23.298V18.453L48.9993 15.393L48.9823 12.35V10.786H52.0593V23.298H48.8293ZM55.7196 23.451C55.2322 23.451 54.7392 23.3717 54.2406 23.213C53.7532 23.0657 53.3566 22.8673 53.0506 22.618L54.1726 20.357C54.3652 20.527 54.5862 20.6573 54.8356 20.748C55.0962 20.85 55.3512 20.901 55.6006 20.901C55.9519 20.901 56.2296 20.8217 56.4336 20.663C56.6376 20.5043 56.8132 20.255 56.9606 19.915L57.3856 18.844L57.6406 18.521L60.7686 10.786H63.8456L59.8676 20.374C59.5502 21.1673 59.1819 21.785 58.7626 22.227C58.3546 22.6803 57.8956 22.9977 57.3856 23.179C56.8869 23.3603 56.3316 23.451 55.7196 23.451ZM56.9776 20.391L52.9146 10.786H56.2296L59.2216 18.232L56.9776 20.391ZM64.6806 20V7.386H67.9106V20H64.6806ZM70.1627 20V8.1H75.7897C77.1043 8.1 78.2603 8.34367 79.2577 8.831C80.255 9.31833 81.0313 10.004 81.5867 10.888C82.1533 11.772 82.4367 12.826 82.4367 14.05C82.4367 15.2627 82.1533 16.3167 81.5867 17.212C81.0313 18.096 80.255 18.7817 79.2577 19.269C78.2603 19.7563 77.1043 20 75.7897 20H70.1627ZM73.5287 17.314H75.6537C76.3337 17.314 76.923 17.1893 77.4217 16.94C77.9317 16.6793 78.3283 16.3053 78.6117 15.818C78.895 15.3193 79.0367 14.73 79.0367 14.05C79.0367 13.3587 78.895 12.7693 78.6117 12.282C78.3283 11.7947 77.9317 11.4263 77.4217 11.177C76.923 10.9163 76.3337 10.786 75.6537 10.786H73.5287V17.314ZM88.6786 20.153C87.6699 20.153 86.7746 19.949 85.9926 19.541C85.2106 19.133 84.5929 18.572 84.1396 17.858C83.6976 17.1327 83.4766 16.3053 83.4766 15.376C83.4766 14.4467 83.6976 13.625 84.1396 12.911C84.5929 12.197 85.2106 11.6417 85.9926 11.245C86.7746 10.837 87.6699 10.633 88.6786 10.633C89.6872 10.633 90.5826 10.837 91.3646 11.245C92.1579 11.6417 92.7756 12.197 93.2176 12.911C93.6596 13.625 93.8806 14.4467 93.8806 15.376C93.8806 16.3053 93.6596 17.1327 93.2176 17.858C92.7756 18.572 92.1579 19.133 91.3646 19.541C90.5826 19.949 89.6872 20.153 88.6786 20.153ZM88.6786 17.586C89.0526 17.586 89.3812 17.501 89.6646 17.331C89.9592 17.161 90.1916 16.9117 90.3616 16.583C90.5316 16.243 90.6166 15.8407 90.6166 15.376C90.6166 14.9113 90.5316 14.5203 90.3616 14.203C90.1916 13.8743 89.9592 13.625 89.6646 13.455C89.3812 13.285 89.0526 13.2 88.6786 13.2C88.3159 13.2 87.9872 13.285 87.6926 13.455C87.4092 13.625 87.1769 13.8743 86.9956 14.203C86.8256 14.5203 86.7406 14.9113 86.7406 15.376C86.7406 15.8407 86.8256 16.243 86.9956 16.583C87.1769 16.9117 87.4092 17.161 87.6926 17.331C87.9872 17.501 88.3159 17.586 88.6786 17.586ZM100.086 20.153C99.0658 20.153 98.1535 19.949 97.3488 19.541C96.5555 19.133 95.9322 18.572 95.4788 17.858C95.0255 17.1327 94.7988 16.3053 94.7988 15.376C94.7988 14.4467 95.0255 13.625 95.4788 12.911C95.9322 12.197 96.5555 11.6417 97.3488 11.245C98.1535 10.837 99.0658 10.633 100.086 10.633C101.129 10.633 102.03 10.854 102.789 11.296C103.548 11.738 104.087 12.3613 104.404 13.166L101.905 14.441C101.69 14.0103 101.423 13.6987 101.106 13.506C100.789 13.302 100.443 13.2 100.069 13.2C99.6948 13.2 99.3548 13.285 99.0488 13.455C98.7428 13.625 98.4992 13.8743 98.3178 14.203C98.1478 14.5203 98.0628 14.9113 98.0628 15.376C98.0628 15.852 98.1478 16.2543 98.3178 16.583C98.4992 16.9117 98.7428 17.161 99.0488 17.331C99.3548 17.501 99.6948 17.586 100.069 17.586C100.443 17.586 100.789 17.4897 101.106 17.297C101.423 17.093 101.69 16.7757 101.905 16.345L104.404 17.62C104.087 18.4247 103.548 19.048 102.789 19.49C102.03 19.932 101.129 20.153 100.086 20.153ZM108.969 20.153C108.187 20.153 107.422 20.0623 106.674 19.881C105.937 19.6997 105.342 19.473 104.889 19.201L105.858 16.991C106.289 17.2517 106.793 17.4613 107.371 17.62C107.949 17.7673 108.516 17.841 109.071 17.841C109.615 17.841 109.989 17.7843 110.193 17.671C110.408 17.5577 110.516 17.4047 110.516 17.212C110.516 17.0307 110.414 16.9003 110.21 16.821C110.017 16.7303 109.757 16.6623 109.428 16.617C109.111 16.5717 108.759 16.5207 108.374 16.464C107.989 16.4073 107.598 16.3337 107.201 16.243C106.816 16.141 106.459 15.9937 106.13 15.801C105.813 15.597 105.558 15.325 105.365 14.985C105.172 14.645 105.076 14.2143 105.076 13.693C105.076 13.1037 105.246 12.5823 105.586 12.129C105.937 11.6643 106.447 11.3017 107.116 11.041C107.785 10.769 108.601 10.633 109.564 10.633C110.21 10.633 110.862 10.701 111.519 10.837C112.188 10.9617 112.749 11.1543 113.202 11.415L112.233 13.608C111.78 13.3473 111.326 13.1717 110.873 13.081C110.42 12.979 109.989 12.928 109.581 12.928C109.037 12.928 108.652 12.9903 108.425 13.115C108.21 13.2397 108.102 13.3927 108.102 13.574C108.102 13.7553 108.198 13.897 108.391 13.999C108.584 14.0897 108.839 14.1633 109.156 14.22C109.485 14.2653 109.842 14.3163 110.227 14.373C110.612 14.4183 110.998 14.492 111.383 14.594C111.78 14.696 112.137 14.849 112.454 15.053C112.783 15.2457 113.043 15.512 113.236 15.852C113.429 16.1807 113.525 16.6057 113.525 17.127C113.525 17.6937 113.349 18.2037 112.998 18.657C112.658 19.1103 112.148 19.473 111.468 19.745C110.799 20.017 109.966 20.153 108.969 20.153Z" fill="white"/>
                </svg>
            </div>
            <div class="nav-section">
                <a href="?page=home#home" class="nav-link">Главная</a>
                <a href="?page=home#tasks" class="nav-link">Задача</a>
                <a href="?page=home#solution" class="nav-link">AI-решение</a>
                <a href="?page=demo" class="nav-link">Demo</a>
            </div>
            <div class="learn-more">
                <a href="?page=demo"><button class="outline-button">Попробовать Демо</button></a>
            </div>
            <input type="checkbox" id="hamburger-checkbox" class="hamburger-checkbox">
            <label for="hamburger-checkbox" class="hamburger-label">
                <span></span>
                <span></span>
                <span></span>
            </label>
            <div class="mobile-menu">
               <label for="hamburger-checkbox" class="mobile-nav-link">
                 <a href="?page=home#home">Главная</a>
               </label>
               <label for="hamburger-checkbox" class="mobile-nav-link">
                 <a href="?page=home#tasks">Задача</a>
               </label>
               <label for="hamburger-checkbox" class="mobile-nav-link">
                 <a href="?page=home#solution">AI-решение</a>
               </label>
               <label for="hamburger-checkbox" class="mobile-nav-link">
                 <a href="?page=demo">Demo</a>
               </label>
            </div>
        </div>

    """, unsafe_allow_html=True)
    st.markdown("""
    <script>
    function initHeader() {
        function closeMenu() {
            const checkbox = document.getElementById('hamburger-checkbox');
            if (checkbox) checkbox.checked = false;
        }

        function scrollTo(targetId) {
            const element = document.querySelector(targetId);
            if (element) {
                element.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }

        function handleLinkClick(e) {
            const href = this.getAttribute('href');
            
            if (href.startsWith('#')) {
                e.preventDefault();
                closeMenu();
                setTimeout(() => scrollTo(href), 100);
            } else if (href.startsWith('?page=')) {
                e.preventDefault();
                closeMenu();
                
                if (href.includes('#')) {
                    const [pagePart, anchorPart] = href.split('#');
                    window.location.href = pagePart;
                    setTimeout(() => {
                        if (anchorPart) {
                            scrollTo('#' + anchorPart);
                        }
                    }, 100);
                } else {
                    window.location.href = href;
                }
            }
        }

        document.querySelectorAll('a[href^="#"], a[href^="?page="]').forEach(link => {
            link.addEventListener('click', handleLinkClick);
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initHeader);
    } else {
        initHeader();
    }
    </script>
    """, unsafe_allow_html=True)

