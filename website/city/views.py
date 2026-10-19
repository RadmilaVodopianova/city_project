from django.http import HttpResponse


# Общее оформление и меню для всех страниц
def page(title, content):
    return HttpResponse(f"""
        <!DOCTYPE html>
        <html lang="uk">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                  content="width=device-width, initial-scale=1">
            <title>{title} — Одеса</title>

            <style>
                * {{
                    box-sizing: border-box;
                }}

                body {{
    margin: 0;
    min-height: 100vh;
    background: linear-gradient(
        90deg,
        #df666b 0%,
        #f5c7c9 25%,
        #ffffff 50%,
        #fff0bb 75%,
        #efc34d 100%
    );
    background-attachment: fixed;
    color: #24384a;
    font-family: Arial, sans-serif;
    line-height: 1.7;
}}

                header {{
                    background: #17354a;
                    color: #fffaf0;
                    padding: 36px 24px;
                }}

                .header-inner {{
                    max-width: 1100px;
                    margin: 0 auto;
                }}

                .brand {{
                    color: #fffaf0;
                    font-family: Georgia, serif;
                    font-size: 42px;
                    font-weight: bold;
                    text-decoration: none;
                }}

                .tagline {{
                    margin: 4px 0 0;
                    color: #c8d9df;
                    font-size: 15px;
                }}

                nav {{
                    display: flex;
                    flex-wrap: wrap;
                    gap: 8px;
                    margin-top: 24px;
                }}

                nav a {{
                    padding: 9px 14px;
                    border: 1px solid #567080;
                    border-radius: 8px;
                    color: #fffaf0;
                    text-decoration: none;
                    font-size: 14px;
                    transition: background 0.2s, color 0.2s;
                }}

                nav a:hover,
                nav a:focus-visible {{
                    background: #e7c88e;
                    color: #17354a;
                    border-color: #e7c88e;
                }}

                main {{
                    max-width: 1100px;
                    margin: 36px auto;
                    padding: 36px;
                    background: #ffffff;
                    border: 1px solid #e3e5e4;
                    border-radius: 16px;
                    box-shadow: 0 10px 30px rgba(23, 53, 74, 0.06);
                    overflow-wrap: anywhere;
                }}

                h1, h2 {{
                    font-family: Georgia, serif;
                    line-height: 1.25;
                    color: #17354a;
                }}

                h1 {{
                    margin: 0 0 24px;
                    font-size: clamp(30px, 5vw, 46px);
                }}

                h2 {{
                    margin: 28px 0 14px;
                    font-size: 26px;
                }}

                p {{
                    margin: 14px 0;
                }}

                main a {{
                    color: #17647a;
                    text-underline-offset: 4px;
                }}

                main a:hover {{
                    color: #925e1d;
                }}

                ul {{
                    padding-left: 24px;
                }}

                li {{
                    margin-bottom: 14px;
                    padding-left: 5px;
                }}

                li::marker {{
                    color: #b98740;
                }}

                article {{
                    margin: 24px 0;
                    padding: 24px;
                    border-left: 4px solid #d5b77e;
                    border-radius: 0 12px 12px 0;
                    background: #f8f7f3;
                }}

                article h2 {{
                    margin-top: 0;
                }}

                time {{
                    color: #617380;
                    font-size: 14px;
                }}

                img {{
                    display: block;
                    border-radius: 12px;
                    border: 1px solid #e3e5e4;
                    margin: 20px 0;
                }}

                hr {{
                    margin: 30px 0;
                    border: 0;
                    border-top: 1px solid #e3e5e4;
                }}

                footer {{
                    padding: 0 24px 32px;
                    text-align: center;
                    color: #617380;
                    font-size: 14px;
                }}

                @media (max-width: 600px) {{
                    header {{
                        padding: 24px 16px;
                    }}

                    .brand {{
                        font-size: 34px;
                    }}

                    nav a {{
                        padding: 8px 11px;
                    }}

                    main {{
                        margin: 20px 12px;
                        padding: 24px 18px;
                    }}

                    article {{
                        padding: 18px;
                    }}
                }}
            </style>
        </head>

        <body>
            <header>
                <div class="header-inner">
                    <a class="brand" href="/">Одеса.</a>
                    <p class="tagline">
                        Місто біля моря. Історії, люди та спадщина.
                    </p>

                    <nav aria-label="Головне меню">
                        <a href="/">Головна</a>
                        <a href="/news/">Новини</a>
                        <a href="/management/">Голови міста</a>
                        <a href="/facts/">Факти</a>
                        <a href="/contacts/">Контакти</a>
                        <a href="/history/">Історія</a>
                        <a href="/history/people/">Відомі мешканці</a>
                        <a href="/history/photos/">Історичні фото</a>
                    </nav>
                </div>
            </header>

            <main>
                {content}
            </main>

            <footer>
                Навчальний проєкт про Одесу · Django
            </footer>
        </body>
        </html>
    """)


# Головна сторінка
def index(request):
    return page("Головна", """
        <h1>Одеса</h1>
        <h2>Головна</h2>
        <p>Ласкаво просимо на сайт про Одесу!</p>
        <p>Тут ви знайдете новини, цікаві факти,
        історію міста та контакти міських служб.</p>
    """)


# Новини міста
def news(request):
    return page("Новини", """
        <h1>Новини Одеси</h1>
        <p>Архів міських новин</p>

        <article>
            <h2>Історичний центр Одеси внесено
            до списку Світової спадщини ЮНЕСКО</h2>

            <p><time datetime="2023-01-25">25 січня 2023 року</time></p>

            <p>Комітет всесвітньої спадщини ухвалив рішення
            включити історичний центр Одеси до списку
            Світової спадщини ЮНЕСКО.</p>

            <p>Це рішення визнає визначну універсальну
            цінність історичного центру міста.</p>

            <a href="https://whc.unesco.org/en/news/2518/"
               target="_blank" rel="noopener noreferrer">
                Читати повідомлення ЮНЕСКО
            </a>
        </article>
    """)


# Керівництво міста
def management(request):
    return page("Голови міста", """
        <h1>Голови міста Одеси</h1>
        <p>Історичні постаті міського самоврядування.</p>

        <article>
            <h2>Григорій Маразлі</h2>
            <p><strong>Міський голова у 1878–1895 роках.</strong></p>
            <p>За його головування розвивалися міський транспорт,
            освіта та медичні заклади. Як меценат він фінансував
            будівництво й придбання будівель для потреб міста.</p>
            <a href="https://esu.com.ua/article-63553"
               target="_blank" rel="noopener noreferrer">
                Докладніше про Григорія Маразлі
            </a>
        </article>

        <hr>

        <article>
            <h2>Валер’ян Лігін</h2>
            <p><strong>Міський голова у 1895–1896 роках.</strong></p>
            <p>Математик і фахівець у галузі кінематики.
            Працював професором Новоросійського університету
            в Одесі, а згодом очолював місто.</p>
            <a href="https://esu.com.ua/article-55425"
               target="_blank" rel="noopener noreferrer">
                Докладніше про Валер’яна Лігіна
            </a>
        </article>
    """)


# Факти про місто
def facts(request):
    return page("Факти", """
        <h1>Факти про Одесу</h1>
        <ul>
            <li>Одеса розташована на узбережжі Чорного моря.</li>
            <li>Місто є адміністративним центром Одеської області.</li>
            <li>Одна з відомих пам’яток міста — Одеський оперний театр.</li>
        </ul>
    """)


# Контактні телефони
def contacts(request):
    return page("Контакти", """
        <h1>Контактні телефони міських служб</h1>
        <h2>Одеса</h2>
        <ul>
            <li>Єдиний центр звернень громадян: 15-35</li>
            <li>Телефон центру: (048) 705-55-55</li>
            <li>Пожежна охорона та рятувальники: 101</li>
        </ul>
    """)


# Загальна історія міста
def history(request):
    return page("Історія", """
        <h1>Історія Одеси</h1>
        <p>Одеса — портове місто на узбережжі Чорного моря.</p>
        <p>У різні періоди її розвиток був пов’язаний
        із морською торгівлею, культурою та освітою.</p>
        <p>Історія міста відображена в його архітектурі,
        музеях і житті відомих мешканців.</p>
    """)


# Відомі мешканці
def history_people(request):
    return page("Відомі мешканці", """
        <h1>Відомі мешканці Одеси</h1>
        <ul>
            <li>Леонід Утьосов — співак та актор, народився в Одесі.</li>
            <li>Ісаак Бабель — письменник, народився в Одесі.</li>
            <li>Кіра Муратова — кінорежисерка,
            жила та працювала в Одесі.</li>
        </ul>
    """)


# Історичні фотографії
def history_photos(request):
    return page("Історичні фото", """
        <h1>Історичні фотографії Одеси</h1>

        <h2>Пам’ятник Дюку де Рішельє</h2>
        <img
            src="/static/city/images/duke_old.jpg"
            alt="Історичний вид пам’ятника Дюку де Рішельє"
            style="max-width: 100%; width: 700px; height: auto;"
        >
        <p>Джерело: old.odessa.ua.</p>

        <h2>Потьомкінські сходи</h2>
        <img
            src="/static/city/images/stairs_old.jpg"
            alt="Історичний вид Потьомкінських сходів"
            style="max-width: 100%; width: 700px; height: auto;"
        >
        <p>Джерело: Wikimedia Commons.</p>
    """)