from build import img, page, marquee, write, carousel, LIGHTBOX_HTML

# ============================================================ HOME
def build_home():
    body = f"""
<section class="hero">
  <img class="hero-bg" src="{img('GAL_7')}" alt="The Empire Studio live room">
  <div class="hero-content">
    <div class="hero-tagline">East London Recording Studio</div>
    <h1>The Sound<br>of Perfection</h1>
    <p class="lede" style="max-width:560px">World-class acoustics, state-of-the-art equipment and a
    1,500 sq ft live room inside a converted East London church — built to seat a full 40-piece
    orchestra without compromise.</p>
    <div class="hero-actions">
      <a href="contact.html" class="btn btn-primary">Book Now</a>
      <a href="equipment.html" class="btn btn-outline">Explore the Studio</a>
    </div>
  </div>
</section>

{marquee(["Film", "TV", "Game Soundtracks", "Independent Artists", "Orchestras"])}

<section>
  <div class="container">
    <div class="stats">
      <div class="stat"><div class="stat-num">153m²</div><div class="stat-label">Largest live room in East London</div></div>
      <div class="stat"><div class="stat-num">40</div><div class="stat-label">Musicians seated comfortably</div></div>
      <div class="stat"><div class="stat-num">30ft</div><div class="stat-label">Vaulted pine ceiling</div></div>
      <div class="stat"><div class="stat-num">1873</div><div class="stat-label">Former Methodist church</div></div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="split">
      <div>
        <div class="eyebrow">State-of-the-Art Equipment</div>
        <h2>Built for Scoring<br>to Picture</h2>
        <p class="lede">With spacious seating arrangements and top-of-the-line equipment, we ensure that
        every musician feels at ease and can deliver their best performance.</p>
        <p>Digital Recording: AVID Pro Tools HDX · Console: LOOPTROTTER 40-input in-line ·
        Pre Amps: Neve 88R, Neve 1073, API 512V/312 · EQ/Dynamics: Rupert Neve Designs 551, SSL 611EQ ·
        Microphones: Neumann U87 Ai, Telefunken ELA M260/TF51/M60 FET, Peluso P67, Schoeps Mk21 ·
        Monitoring: ATC SCM45a. Acoustic design by Roger D'Arcy.</p>
        <a href="equipment.html" class="btn btn-outline btn-sm">Full Gear List</a>
      </div>
      <img src="{img('Control_Room_001')}" alt="Control room mixing desk and studio monitors at The Empire Studio">
    </div>
  </div>
</section>

<section class="tight bg-alt">
  <div class="container">
    <div class="split reverse">
      <div>
        <div class="eyebrow">Experienced Sound Engineers</div>
        <h2>Trusted By Artists<br>Worldwide</h2>
        <p class="lede">Our engineers have collaborated with artists like Arctic Monkeys, Taylor Swift
        and Michael Bublé, and worked on major TV/film projects including Doctor Who, the BBC and
        Netflix productions.</p>
        <p>Nestled in East London, Empire Studio comfortably accommodates orchestras and large
        ensembles, seating up to 40 musicians. Bathed in natural light, our live room and control
        room inspire creativity — fully equipped for scoring to picture without compromising quality.
        A dedicated vocal booth and amp/soloist booth make it ideal for anything from full orchestras
        to solo performances.</p>
      </div>
      <img src="{img('33a_Wadeson_Street-11')}" alt="The Empire Studio live room and balcony">
    </div>
  </div>
</section>

<section id="services">
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Our Services</div>
      <h2>Exceptional Music Services,<br>Tailored to You</h2>
    </div>
    <div class="grid grid-3">
      <div class="card">
        <span class="card-icon">01 / Score</span>
        <h3>Music to Picture</h3>
        <p>Expert composition and scoring for films, TV shows and commercials — music that
        complements the visuals and elevates the storytelling.</p>
      </div>
      <div class="card">
        <span class="card-icon">02 / Ensemble</span>
        <h3>Orchestral &amp; Choir</h3>
        <p>Fully equipped for full orchestras and ensembles up to 40 players, or 40 vocalists in
        our spacious, naturally lit live room.</p>
      </div>
      <div class="card">
        <span class="card-icon">03 / Keys</span>
        <h3>Piano Sessions</h3>
        <p>Experience the iconic sound and dynamics of our Steinway &amp; Sons Model B Grand Piano —
        also available for practice sessions.</p>
      </div>
      <div class="card">
        <span class="card-icon">04 / Live</span>
        <h3>Remote &amp; Live Video</h3>
        <p>Streaming 32-bit PCM multichannel audio in real time from any DAW via Listento, so you
        can collaborate globally.</p>
      </div>
      <div class="card">
        <span class="card-icon">05 / Cast</span>
        <h3>Podcasts</h3>
        <p>Record in a beautiful, naturally lit, acoustically tuned environment with full RGB LED
        stage lighting — theatre seating allows a live audience.</p>
      </div>
      <div class="card">
        <span class="card-icon">06 / Band</span>
        <h3>Bands &amp; Artists</h3>
        <p>Capture your band's unique sound at East London's ultimate recording destination —
        ask us what 86TVs recorded here.</p>
      </div>
    </div>
  </div>
</section>

<section class="bg-alt tight">
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Recorded Here</div>
    </div>
  </div>
  {marquee(["Taylor Swift", "Michael Bublé", "Sony Music", "Warner Music", "London Symphony Orchestra", "Arctic Monkeys", "Noah And The Whale", "PJ Harvey", "BBC (Dr Who)", "John Lunn"])}
</section>

<section>
  <div class="container">
    <div class="quote">
      <span class="quote-mark">&ldquo;</span>
      <p class="lede">Empire features a fantastic live room where I have had the luck to record the
      best Strings Players in London. The acoustic is ideal for recording strings for films and
      chamber music: the sound is warm and flattering!</p>
      <div class="quote-attr"><strong>Maurizio Malagnini</strong> — Composer, Call The Midwife</div>
    </div>
    <div style="text-align:center;margin-top:32px">
      <a href="testimonials.html" class="btn btn-outline btn-sm">Read More Testimonials</a>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Book a Visit</h2>
    <p class="lede" style="max-width:560px;margin:0 auto 32px">153 Sq M of East London's finest live
    room is waiting. Tell us what you're recording.</p>
    <a href="contact.html" class="btn btn-primary">Contact Us</a>
  </div>
</section>
"""
    write("index.html", page(
        "index.html", "Recording Studio East London",
        "Recording studio in East London with a 153 sqm live room, professional equipment and "
        "control room built for orchestras, bands, podcasts and music-to-picture. Book The Empire "
        "Studio today.",
        body,
        keywords="recording studio east london, live room london, control room, professional "
                 "equipment, music studio east london, recording studio london",
        og_image=img('GAL_7'),
    ))


# ============================================================ ABOUT
def build_about():
    body = f"""
<section class="hero hero-small">
  <img class="hero-bg" src="{img('Empire_About_Us_2')}" alt="Vaulted live room ceiling lit in pink at The Empire Studio, East London">
  <div class="hero-content">
    <div class="hero-tagline">About Us</div>
    <h1>The Studio</h1>
  </div>
</section>

<section>
  <div class="container">
    <div class="split">
      <div>
        <div class="eyebrow">Acoustic Design</div>
        <h2>By The Legendary<br>Roger D'Arcy</h2>
        <p class="lede">Every inch of EBC has been acoustically treated by renowned architect Roger
        D'Arcy, ensuring unparalleled sound quality. Whether you're recording an album, filming a
        music video or staging a photoshoot, EBC delivers an exceptional experience with its full
        blackout facility and impeccable acoustics.</p>
        <p>Roger D'Arcy is an architect and acoustic designer with over 30 years of experience in
        the planning and architectural-acoustic design of recording studios. He's founder of
        Recording Architecture (RA), a UK-based firm specialising in studio design, and co-author of
        "Acoustic Design for the Home Studio" with Hugh Flynn. Beyond his architectural work, D'Arcy
        is also a singer/songwriter, having released solo albums including "Crooked Tales" (2016),
        "House of Heads" (2017) and "The Road To Stameen" (2019).</p>
        <p>D'Arcy has designed studios in over 40 countries. Notable projects include Lansdowne
        Studios, CTS Studios, installations for Abbey Road, studios for EMI Music, Crystalphonic and
        Optimum Mastering.</p>
      </div>
      <img src="{img('33a_Wadeson_Street-11')}" alt="EBC live room, acoustically designed by Roger D'Arcy">
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="split reverse">
      <div>
        <div class="eyebrow">East London's Premier Recording Studio</div>
        <h2>A Historic Church,<br>Reimagined</h2>
        <p class="lede">EBC Studio positions itself as a premier destination for high-quality music
        production, offering a unique combination of cutting-edge technology and artistic ambiance —
        created by Marlon Brown, with acoustic design by Roger D'Arcy.</p>
        <p>Originally a historic Methodist church, the building has been transformed into a
        state-of-the-art, 1,500 sq ft soundproof live room, featuring a dramatic 30-foot-high pine
        vaulted ceiling and a unique surrounding balcony — designed to cater to everything from large
        orchestral recordings to intimate solo sessions.</p>
      </div>
      <img src="{img('Empire_About_Us_2')}" alt="EBC live room vaulted ceiling">
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Come See The Room</h2>
    <a href="contact.html" class="btn btn-primary">Book Now</a>
  </div>
</section>
"""
    write("about-us.html", page(
        "about-us.html", "About Us",
        "The Empire Studio's live room in East London was acoustically designed by renowned "
        "architect Roger D'Arcy inside a converted 1873 Methodist church, with a 30ft vaulted "
        "pine ceiling.",
        body,
        keywords="live room london, recording studio east london, acoustic design, roger d'arcy, "
                 "east london music studio",
        og_image=img('Empire_About_Us_2'),
    ))


# ============================================================ EQUIPMENT
EQUIP_CATS = [
    ("Digital Recording", [("AVID Pro Tools HDX", ""), ("AVID HDX 16 Analog I/O", "×3"), ("AVID Sync HD", ""), ("Mac Pro (2019)", ""), ("Mac Mini (2020) — Zoom, Source Connect, Audio Movers", "")]),
    ("Console", [("LOOPTROTTER 40 Input In-Line Console", "")]),
    ("Pre Amps", [("Neve 88R", "×8"), ("Neve 1073", "×4"), ("API 512V", "×2"), ("API 312", "×2"), ("DAV BG501", "×8")]),
    ("EQ / Dynamics", [("Rupert Neve Designs 551", "×2"), ("SSL 611EQ", "×4"), ("DAV BG503", "×4"), ("Elysia XFilter", "×1")]),
    ("Microphones", [("Neumann U87 Ai", ""), ("Telefunken ELA M260 (omni/card/hyper)", "×3"), ("Telefunken TF51", ""), ("Peluso P67", "×2"), ("Schoeps Mk21", "×2"), ("Telefunken M60 FET", "×6"), ("Austrian Audio OC818", "×5"), ("Austrian Audio OC18", "×5"), ("AEA R84 Ribbon", "×2"), ("Coles 4038", "×1"), ("AKG C451B", "×2"), ("Shure SM57", "×5"), ("Sennheiser MD421 II", "×3"), ("Audix D6", "×1"), ("Warm Audio WA-84 (+omni capsules)", "×4")]),
    ("Monitoring", [("ATC SCM45a", ""), ("PreSonus HP60 6-Channel Headphone Mixing", "×2")]),
    ("Outboard / FX", [("Bricasti M7", ""), ("DAV BG2 4ch Pre Amp", "×2"), ("Behringer ADA8200 8in/8out ADAT", ""), ("ART MX822 8ch Stereo Mixer w/ FX loop", "×3")]),
    ("Video &amp; Lighting", [("Blackmagic Micro Studio Camera 4K (live feed)", ""), ("Control room displays for live feed/picture playback", ""), ("Full lighting rig — ChamSys QuickQ DMX console", "")]),
    ("Instruments &amp; Backline", [("Steinway &amp; Sons Model B Concert Grand", ""), ("Bass Amp: Ampeg 1966 B15", ""), ("Guitar Amp: Fender Deluxe", ""), ("Drums: 1973 Ludwig kit", "")]),
    ("Stands &amp; Seating", [("Music stands (short / tall)", "×40"), ("Chairs", "×40")]),
]

def build_equipment():
    col_html = ["", ""]
    for idx, (name, items) in enumerate(EQUIP_CATS):
        rows = "".join(f'<li><span>{n}</span>{("<b>"+q+"</b>") if q else ""}</li>' for n, q in items)
        col_html[idx % 2] += (
            f'<details class="equip-cat">'
            f'<summary><h3>{name}</h3><span class="equip-toggle-icon"></span></summary>'
            f'<ul>{rows}</ul></details>\n'
        )
    cats_html = f'<div class="equip-col">{col_html[0]}</div><div class="equip-col">{col_html[1]}</div>'

    body = f"""
<section class="hero hero-small">
  <img class="hero-bg" src="{img('Control_Room_003')}" alt="Wood-panelled control room with outboard gear at The Empire Studio">
  <div class="hero-content">
    <div class="hero-tagline">The Gear</div>
    <h1>Equipment List</h1>
  </div>
</section>

<section class="tight equip-intro">
  <div class="container">
    <div class="section-head">
      <p class="lede">Everything at EBC is chosen to disappear behind the performance — vintage
      character where it counts, transparent modern conversion where it matters, and enough channel
      count to record a full orchestra in one pass.</p>
    </div>
  </div>
</section>

<section class="tight bg-alt equip-list">
  <div class="container">
    <div class="equip-grid">
      {cats_html}
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="split reverse">
      <div>
        <div class="eyebrow">The Centrepiece</div>
        <h2>Steinway &amp; Sons<br>Model B Grand</h2>
        <p class="lede">A symbol of unparalleled craftsmanship and sonic brilliance, offering
        musicians an exceptional range of tonal possibilities — from a delicate classical piece to
        powerful jazz improvisation.</p>
        <p>Our acoustically treated live room ensures every note resonates with clarity and depth,
        making it ideal for both solo performances and ensemble recordings.</p>
      </div>
      <img src="{img('steinway_and_marlon')}" alt="Steinway & Sons grand piano being played in the live room">
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>See The Full Floor Plan</h2>
    <p class="lede" style="max-width:520px;margin:0 auto 32px">Explore the complete room layout across
    all three floors — live room, control room, mezzanine and balcony.</p>
    <a href="assets/img/floorplan-wadeson-street.jpg" class="btn btn-primary lightbox-trigger">View Floor Plan</a>
  </div>
</section>
{LIGHTBOX_HTML}
"""
    write("equipment.html", page(
        "equipment.html", "Equipment & Control Room",
        "Explore the professional equipment at our East London recording studio: Neve and API "
        "preamps, a 40-channel console, Neumann microphones and a fully treated control room.",
        body,
        keywords="professional equipment, control room, recording studio equipment, neve preamps, "
                 "recording studio east london, live room london",
        og_image=img('Control_Room_003'),
    ))


# ============================================================ TESTIMONIALS
TESTIMONIALS = [
    ("Empire features a fantastic live room where I have had the luck to record the best Strings Players in London: I have seen them enjoying playing music there, enjoying the space, the sound and the natural light in the room. The acoustic is ideal for recording Strings for films and Chamber Music: the sound is warm and flattering!", "Maurizio Malagnini", "Composer — Call The Midwife"),
    ("Empire studios is a fantastic new addition to the recording scene here in London. Having to compete with some of the best studios in the world it can certainly hold its head up high.", "John Lunn", "Composer — Downton Abbey, Grantchester, The Last Kingdom, Shetland, Jamestown &amp; more"),
    ("I recorded my score for True Things at Empire and it was a wonderful experience. The gorgeous sounding room, the natural light throughout, the great people... the musicians in the string quartet were especially taken by the acoustics to perform in. Can't wait to go back to record there again.", "Alex Baranowski", "True Things"),
    ("Empire Studio is a welcome and much needed addition to the London studio scene, filling a gap in the market between Abbey Road, AIR Lyndhurst and RAK Studios. London now has another fantastic sounding large room. The team working there are top notch, friendly and welcoming.", "Guy Chambers", "Robbie Williams (Sky Film)"),
    ("I've recorded an 18 piece classical choir, a rock band for Bat Out Of Hell the musical, a string section, and filmed some music educational videos. The studio and staff have always been brilliant but also highly accommodating. I'd be totally happy to recommend them.", "Rob Emery", "Pianist, Conductor &amp; Orchestrator"),
    ("We recorded part of the Horizon Zero Dawn Forbidden West main theme, and cut scenes, at Empire Studios. It's a lovely sounding room, with great gear, and a lovely team to work with. I recommend wholeheartedly.", "Peter Michael Davison", "Composer, Conductor &amp; Orchestrator"),
]

def build_testimonials():
    cards = ""
    for quote, name, role in TESTIMONIALS:
        cards += f"""<div class="quote">
      <span class="quote-mark">&ldquo;</span>
      <p>{quote}</p>
      <div class="quote-attr"><strong>{name}</strong> — {role}</div>
    </div>\n"""

    body = f"""
<section class="hero hero-small">
  <img class="hero-bg" src="{img('Control_Room_009')}" alt="Control room viewed from the live room at The Empire Studio">
  <div class="hero-content">
    <div class="hero-tagline">Kind Words</div>
    <h1>Testimonials</h1>
  </div>
</section>

<section>
  <div class="container">
    {carousel(cards, "quote-scroller")}
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Add Your Story</h2>
    <a href="contact.html" class="btn btn-primary">Book a Session</a>
  </div>
</section>
"""
    write("testimonials.html", page(
        "testimonials.html", "Testimonials",
        "Hear from composers, engineers and artists who've recorded in our East London live room "
        "and control room, from film scores to chart-topping albums.",
        body,
        keywords="recording studio east london, live room london, control room, testimonials, "
                 "recording studio reviews",
        og_image=img('Control_Room_009'),
    ))


# ============================================================ GALLERY
GALLERY_IMAGES = [
    ("GAL_3", "tall", "Kitchen and lounge area with upright piano and red bar stools at The Empire Studio"),
    ("Control_Room_001", "", "Control room mixing desk and studio monitors at The Empire Studio, East London"),
    ("GAL_7", "wide", "Vaulted pine ceiling of the live room lit in pink, converted from a Victorian church"),
    ("33a_Wadeson_Street-11", "tall", "Full view of the live room with staircase, sofas and lounge seating"),
    ("Control_Room_003", "", "Wood-panelled control room booth with speakers and outboard gear"),
    ("Marlon_and_S_S__107_", "", "Close-up of the Steinway & Sons grand piano nameplate"),
    ("GAL_4", "wide", "Piano bar lounge area with red stools and upright piano"),
    ("Control_Room_009", "", "Control room viewed through the glass from the live room"),
    ("GAL_6", "tall", "Kitchen with exposed brick wall and New York skyline artwork"),
    ("Marlon_and_S_S__2_", "", "Lounge and office space with staircase and vintage decor"),
    ("Empire_About_Us_2", "wide", "Vaulted live room ceiling bathed in pink stage lighting"),
    ("GAL_5", "tall", "Vaulted live room with neon sign and staircase to the mezzanine"),
    ("Marlon_and_S_S__24_", "", "Steinway grand piano interior showing strings and hammers"),
    ("Marlon_and_S_S__58_", "", "String quartet recording session in the live room"),
    ("Marlon_and_S_S__65_", "", "Collage of a live recording session: string players, an engineer at the console, and a dancer performing beside the piano"),
]

SHAPE_SPANS = {"tall": (1, 2), "wide": (2, 1), "": (1, 1)}


def pack_tiles(sizes, rows=2):
    """Deterministic gap-free placement: first-fit column scan, guarantees no holes."""
    occupied = set()
    placements = []
    for size in sizes:
        cspan, rspan = SHAPE_SPANS[size]
        c = 0
        while True:
            placed_row = None
            for r in range(0, rows - rspan + 1):
                if all((cc, rr) not in occupied for cc in range(c, c + cspan) for rr in range(r, r + rspan)):
                    placed_row = r
                    break
            if placed_row is not None:
                for cc in range(c, c + cspan):
                    for rr in range(placed_row, placed_row + rspan):
                        occupied.add((cc, rr))
                placements.append((c, placed_row, cspan, rspan))
                break
            c += 1
    return placements


def build_gallery():
    placements = pack_tiles([size for _, size, _ in GALLERY_IMAGES])
    imgs = "\n".join(
        f'<a class="lightbox-trigger" style="grid-column:{c+1} / span {cspan}; grid-row:{r+1} / span {rspan};" href="{img(name)}">'
        f'<img src="{img(name)}" alt="{alt}" loading="lazy"></a>'
        for (name, size, alt), (c, r, cspan, rspan) in zip(GALLERY_IMAGES, placements)
    )
    body = f"""
<section class="hero hero-small">
  <img class="hero-bg" src="{img('GAL_5')}" alt="Vaulted live room with neon sign at The Empire Studio, East London">
  <div class="hero-content">
    <div class="hero-tagline">Inside The Studio</div>
    <h1>Gallery</h1>
  </div>
</section>

<section class="tight">
  <div class="container">
    {carousel(imgs, "tile-scroll")}
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>See It In Person</h2>
    <a href="contact.html" class="btn btn-primary">Book a Visit</a>
  </div>
</section>
{LIGHTBOX_HTML}
"""
    write("gallery.html", page(
        "gallery.html", "Gallery",
        "See inside The Empire Studio's live room, control room and professional equipment — East "
        "London's premier recording studio in a converted Victorian church.",
        body,
        keywords="recording studio east london, live room london, control room, studio gallery, "
                 "professional equipment",
        og_image=img('GAL_5'),
    ))


# ============================================================ NEWS
ARTICLES = [
    {
        "date": "February 20, 2026",
        "title": "Why Choosing the Right Podcast Studio in London Matters More Than You Think",
        "excerpt": "Podcasting has evolved. It's no longer two people in a bedroom with USB microphones — it's brand strategy, authority building and increasingly, video-first distribution.",
        "img": "GAL_6",
        "body": """<p>Podcasting has evolved. It's no longer two people in a bedroom with USB microphones. It's brand
        strategy, authority building, cinematic storytelling, and increasingly — video-first
        distribution. If you're searching for a podcast studio in London, you're probably past the
        "DIY experiment" stage. You care about quality, presence, and how your show looks and sounds.</p>
        <p><strong>Sound is 80% of your podcast.</strong> You can forgive average video. You cannot
        forgive bad audio. The difference between a carpeted office room, a foam-padded box, and a
        purpose-built live acoustic space is enormous. At The Empire Studio, podcast sessions benefit
        from 30ft vaulted pine ceilings, natural reverb controlled by professional acoustic design,
        isolation where needed, control room-grade monitoring and a full lighting system.</p>
        <p><strong>Video podcasting has changed the game.</strong> Your podcast is no longer just
        audio — it's content infrastructure. A serious setup should include multi-camera recording,
        proper lighting, clean backdrops, real depth in frame and on-site monitoring. Natural
        light — rarely found in London studios — creates a completely different atmosphere on
        camera.</p>
        <p><strong>Hosting with a live audience.</strong> At Empire Studio, the theatre-style layout
        allows you to record in front of guests, capture crowd reactions, host ticketed live
        tapings and film full sessions for distribution — while most London podcast studios cap
        out at 3–4 people.</p>
        <p>Before you book anywhere, ask: is it acoustically treated professionally? Can they handle
        video properly? Is there natural light or only LED panels? Can it scale for audience
        recordings? Because listeners might forgive average ideas — they won't forgive average
        execution.</p>""",
    },
    {
        "date": "October 21, 2024",
        "title": "Creative Uses of EBC Studio's Large Live Room",
        "excerpt": "EBC hosts the largest live room in East London, at 153 sqm. Acoustically designed by Roger D'Arcy, it unlocks a wealth of creative possibilities.",
        "img": "GAL_3",
        "body": """<p>EBC Studio hosts the largest live room in East London, at 153 sq m (15.3 x 10). In music
        production, the space in which music is recorded can significantly impact the final
        product's quality and feel — and Roger D'Arcy's acoustic design balances natural reverb with
        clarity, warmth and space.</p>
        <p><strong>Natural reverb.</strong> The room's architecture allows sound to bloom, travel and
        return with just the right amount of warmth — particularly for drums, strings and vocals —
        often outperforming artificial reverb plugins.</p>
        <p><strong>Orchestras, ensembles and big bands.</strong> Musicians can perform together in
        the space rather than layering parts in isolation, capturing a cohesive, live performance
        feel perfect for film scores, jazz ensembles and live albums.</p>
        <p><strong>Experimental technique.</strong> Producers can place a guitar amp at one end of
        the space and mic it from a distance to create a sense of air, or capture vocals from across
        the room for a distant, haunting effect.</p>
        <p><strong>Foley and sound design.</strong> The acoustics allow for realistic spatial
        recordings that replicate expansive environments — from grand halls to open landscapes —
        ideal for film, TV and game audio.</p>""",
    },
    {
        "date": "October 21, 2024",
        "title": "Why East London is the Ultimate Hub for Musicians and Artists",
        "excerpt": "From grime legends like Dizzee Rascal and Wiley to indie icons like The Libertines, East London has shaped the UK's musical landscape.",
        "img": "Marlon_and_S_S__2_",
        "body": """<p>East London has long been a creative powerhouse — the birthplace of grime, home to indie
        icons like The Libertines and Bloc Party, and a stronghold for techno and electronic music at
        clubs like Fabric, XOYO and Village Underground.</p>
        <p>Grime music emerged from the streets of East London in the early 2000s through artists like
        Dizzee Rascal, Wiley and Kano, raised in Bow — raw, real and reflective of the diverse urban
        life in the area. Meanwhile Shoreditch, Dalston and Hackney nurtured an indie and alternative
        scene, with Bloc Party and The xx cutting their teeth in gritty East End venues.</p>
        <p>Beyond the famous names, East London remains home to niche artists and emerging talent —
        from genre-blending acts like Shygirl and Bakar to the visual artists who have transformed
        Hackney Wick's former industrial spaces into creative studios.</p>
        <p>Our studio, based in the heart of East London, is proud to be part of this creative
        ecosystem — offering competitive rates, flexible booking and a welcoming environment for
        musicians of all genres.</p>""",
    },
    {
        "date": "October 21, 2024",
        "title": "East London's Rising Stars: Musicians and Artists Shaping the Sound of the City",
        "excerpt": "Discover the artists shaping East London's soundscape, and why the area remains a unique incubator for creativity.",
        "img": "GAL_4",
        "body": """<p>East London has always been a cultural melting pot, with a deep history of innovation in
        art, music and fashion — from grime's gritty origins on the streets of Bow and Hackney to
        indie rock and techno.</p>
        <p>Names like Wiley, Dizzee Rascal and Kano laid the foundations of grime, while newer artists
        like Stormzy keep the fire burning. Areas like Shoreditch and Dalston nurtured Bloc Party, The
        Libertines and The xx, and clubs like Fabric and XOYO continue to draw electronic talent from
        around the world.</p>
        <p>What unites the scene is collaboration — musicians, producers, filmmakers and visual artists
        coming together to create cross-disciplinary projects that break down traditional boundaries.
        Studios like ours play a role in facilitating that, offering state-of-the-art equipment and a
        comfortable environment so artists have the tools to create their best work.</p>
        <p>We're passionate about supporting the next generation — providing affordable recording
        options, mentorship and guidance to help new artists navigate the industry.</p>""",
    },
    {
        "date": "May 28, 2019",
        "title": "Hellraiser Soundtrack Recorded at EBC",
        "excerpt": "The haunting soundtrack for 'Hellraiser', composed by Ben Lovett, was recorded in EBC's acoustically treated live room.",
        "img": "Control_Room_009",
        "body": """<p>In the heart of East London, Empire Broadcasting Corporation (EBC) Studio became the
        epicentre of groundbreaking music production for the highly anticipated soundtrack of
        "Hellraiser," composed by Ben Lovett — known for his work on Synchronicity and The Night
        House.</p>
        <p>Lovett's score pays homage to Christopher Young's original neo-gothic compositions while
        introducing new sonic elements. His use of piano melodies juxtaposed with low-frequency
        electronics creates an atmosphere both seductive and sickening.</p>
        <p>Recorded in EBC's state-of-the-art facilities, every note resonates with precision and
        depth — the acoustically treated live room, designed by Roger D'Arcy, captures the full
        spectrum of Lovett's intricate soundscapes, from hauntingly beautiful piano sequences to
        bone-chilling electronic undertones.</p>""",
    },
    {
        "date": "May 28, 2019",
        "title": "A Grand Addition: Steinway Piano Installed at EBC Studio",
        "excerpt": "EBC Studio announces the latest addition to its world-class recording facilities — a magnificent Steinway & Sons grand piano.",
        "img": "Marlon_and_S_S__107_",
        "body": """<p>Empire Broadcasting Corporation (EBC) Studio in East London is thrilled to announce the
        latest addition to its world-class recording facilities — a magnificent Steinway &amp; Sons
        grand piano. Renowned for their unparalleled craftsmanship and exquisite sound, Steinway
        pianos have been the choice of legendary musicians for over a century.</p>
        <p>The Steinway grand piano, known for its rich tonal quality and responsive touch, offers
        artists an exceptional instrument that can elevate any musical project — whether recording a
        classical masterpiece, jazz improvisation or contemporary composition.</p>
        <p>Our acoustically treated live room, designed by acclaimed architect Roger D'Arcy, ensures
        each note resonates with clarity and depth, ideal for both solo performances and ensemble
        recordings.</p>""",
    },
    {
        "date": "May 28, 2019",
        "title": "86TVs Electrifies EBC Studio with Live Performance",
        "excerpt": "86TVs brought tracks like 'Higher Love,' 'Spinning World' and 'Dreaming' to life in a world-class recording environment.",
        "img": "GAL_5",
        "body": """<p>Empire Broadcasting Corporation (EBC) Studio recently played host to an electrifying live
        performance by 86TVs, marking a significant milestone for the band and their fans. The debut
        EP "You Don't Have To Be Yourself Right Now" and single "New Used Car," along with their
        self-titled debut album, are available via Parlophone Records.</p>
        <p>The live session at EBC Studio showcased 86TVs' dynamic energy, bringing tracks like
        "Higher Love," "Spinning World" and "Dreaming" to life in a way that only a world-class
        recording environment can facilitate. Directed by Polocho and produced by Miquel Agell under
        Say Goodnight Films, the video production matched the sonic excellence of EBC's facilities.</p>""",
    },
    {
        "date": "May 28, 2019",
        "title": "Artist Spotlight: Aaron Taylor",
        "excerpt": "Known for his soulful voice and captivating performances, Aaron Taylor has been making waves with his blend of R&B, soul and contemporary sounds.",
        "img": "Marlon_and_S_S__24_",
        "body": """<p>Empire Broadcasting Corporation (EBC) Studio is proud to shine the spotlight on a truly
        exceptional talent — Aaron Taylor. Known for his soulful voice and captivating performances,
        Aaron has been making waves with his unique blend of R&amp;B, soul and contemporary sounds,
        influenced from a young age by legends like Stevie Wonder and Marvin Gaye.</p>
        <p>Aaron graced EBC Studio to work on tracks from his latest album, including "Be Alright," "Wanna
        Be Close" and "Get Through This Together" — collaborating with our in-house engineers to
        bring his vision to life with unparalleled clarity and depth.</p>""",
    },
]

def build_news():
    rows = ""
    for a in ARTICLES:
        rows += f"""<div class="article-row">
      <img src="{img(a['img'])}" alt="{a['title']}">
      <div>
        <span class="article-date">{a['date']}</span>
        <h3>{a['title']}</h3>
        <p>{a['excerpt']}</p>
        <details>
          <summary class="read-more">Read More</summary>
          <div style="margin-top:20px">{a['body']}</div>
        </details>
      </div>
    </div>\n"""

    body = f"""
<section class="hero hero-small">
  <img class="hero-bg" src="{img('GAL_4')}" alt="Piano bar lounge area at The Empire Studio, East London">
  <div class="hero-content">
    <div class="hero-tagline">The Journal</div>
    <h1>News &amp; Stories</h1>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="article-list">
      {rows}
    </div>
  </div>
</section>
"""
    write("news.html", page(
        "news.html", "Journal",
        "News, stories and artist spotlights from The Empire Studio — East London's recording "
        "studio with a professional live room and control room.",
        body,
        keywords="recording studio east london, live room london, music studio news, east london",
        og_image=img('GAL_4'),
    ))


# ============================================================ CONTACT
def build_contact():
    body = f"""
<section class="hero hero-small">
  <img class="hero-bg" src="{img('vlcsnap-2024-08-12-02h10m44s927')}" alt="EBC mixing desk">
  <div class="hero-content">
    <div class="hero-tagline">Get In Touch</div>
    <h1>Let's Make Music</h1>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="split split-top">
      <form class="contact-form" action="mailto:info@ebc.live" method="post" enctype="text/plain">
        <div class="form-grid">
          <div>
            <label for="first_name">First Name</label>
            <input id="first_name" name="first_name" type="text" required>
          </div>
          <div>
            <label for="last_name">Last Name</label>
            <input id="last_name" name="last_name" type="text" required>
          </div>
          <div class="full">
            <label for="email">Email</label>
            <input id="email" name="email" type="email" required>
          </div>
          <div class="full">
            <label class="checkbox-label">
              <input type="checkbox" name="newsletter" value="yes">
              <span>Sign up for news and updates</span>
            </label>
          </div>
          <div>
            <label for="phone">Phone</label>
            <input id="phone" name="phone" type="text">
          </div>
          <div>
            <label for="preferred_date">Preferred Date</label>
            <input id="preferred_date" name="preferred_date" type="date">
          </div>
          <div class="full">
            <label>What services are you interested in?</label>
            <div class="checkbox-grid">
              <label class="checkbox-label"><input type="checkbox" name="services" value="Music to Picture"><span>Music to Picture</span></label>
              <label class="checkbox-label"><input type="checkbox" name="services" value="Orchestra"><span>Orchestra</span></label>
              <label class="checkbox-label"><input type="checkbox" name="services" value="Band"><span>Band</span></label>
              <label class="checkbox-label"><input type="checkbox" name="services" value="Piano Session (recording)"><span>Piano Session (recording)</span></label>
              <label class="checkbox-label"><input type="checkbox" name="services" value="Choir"><span>Choir</span></label>
              <label class="checkbox-label"><input type="checkbox" name="services" value="Rehearsal (Band / Piano / Orchestra/ Choir)"><span>Rehearsal (Band / Piano / Orchestra/ Choir)</span></label>
              <label class="checkbox-label"><input type="checkbox" name="services" value="Filming"><span>Filming</span></label>
              <label class="checkbox-label"><input type="checkbox" name="services" value="Event Hire"><span>Event Hire</span></label>
              <label class="checkbox-label"><input type="checkbox" name="services" value="Podcast"><span>Podcast</span></label>
            </div>
          </div>
          <div>
            <label for="budget">What is your budget?</label>
            <input id="budget" name="budget" type="text" required>
          </div>
          <div>
            <label for="hear_about">How did you hear about us?</label>
            <select id="hear_about" name="hear_about" required>
              <option value="">Select an option</option>
              <option>Word of mouth</option>
              <option>Instagram</option>
              <option>Facebook</option>
              <option>Google or other search engine</option>
              <option>Press / News</option>
              <option>Email</option>
              <option>Twitter</option>
              <option>Recorded here before</option>
            </select>
          </div>
          <div class="full">
            <label for="message">Message</label>
            <textarea id="message" name="message" required></textarea>
          </div>
          <div class="full">
            <button type="submit" class="btn btn-primary">Submit</button>
          </div>
        </div>
      </form>
      <div class="contact-details">
        <div class="contact-item">
          <div class="eyebrow">Visit</div>
          <p>33 Wadeson Street<br>London, E2 9DR<br>United Kingdom</p>
        </div>
        <div class="contact-item">
          <div class="eyebrow">Follow</div>
          <p><a href="http://instagram.com/theempirestudiolondon">@theempirestudiolondon</a></p>
        </div>
        <div class="contact-item">
          <div class="eyebrow">Booking</div>
          <p>Tell us your format, date and headcount and we'll get back to you with availability
          and day rates.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="tight bg-alt">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Find Us</div>
      <h2>33 Wadeson Street</h2>
    </div>
    <div class="map-frame">
      <iframe class="map-embed" src="https://www.google.com/maps?q=33+Wadeson+Street,+London,+E2+9DR,+United+Kingdom&output=embed" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Map to The Empire Studio, 33 Wadeson Street, London"></iframe>
    </div>
    <a class="btn btn-outline btn-sm map-directions" href="https://maps.google.com?q=33 Wadeson Street London, England, E2 9DR United Kingdom" target="_blank" rel="noopener">Get Directions</a>
  </div>
</section>
"""
    write("contact.html", page(
        "contact.html", "Contact & Book",
        "Get in touch to book East London's premier recording studio — live room, control room "
        "and professional equipment for orchestras, bands, podcasts and more.",
        body,
        keywords="recording studio east london, book recording studio, live room london, control "
                 "room, contact recording studio",
        og_image=img('vlcsnap-2024-08-12-02h10m44s927'),
    ))


# ============================================================ EVENTS
def build_events():
    body = f"""
<section class="hero hero-small">
  <img class="hero-bg" src="{img('33a_Wadeson_Street-11')}" alt="Live room with staircase and lounge seating at The Empire Studio">
  <div class="hero-content">
    <div class="hero-tagline">What's On</div>
    <h1>Events</h1>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="event-card">
      <div class="event-date-block">
        <div class="month">February</div>
        <div class="day">27</div>
      </div>
      <div>
        <h3>Candlelit Concert</h3>
        <p>Thursday, 27th February · Live music starts at 7pm, in the heart of EBC's 153 sqm live
        room.</p>
        <div class="event-meta">
          <div>18:30 – 22:00</div>
          <div>Empire Broadcasting Corporation, 33 Wadeson Street, London E2 9DR</div>
        </div>
      </div>
      <div>
        <a class="btn btn-outline btn-sm" href="http://maps.google.com?q=33 Wadeson Street London, England, E2 9DR United Kingdom" target="_blank" rel="noopener">View Map</a>
      </div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Host Your Own Event</h2>
    <p class="lede" style="max-width:520px;margin:0 auto 32px">From candlelit concerts to ticketed
    live podcast tapings, our theatre-style live room can host guests, cameras and a full band.</p>
    <a href="contact.html" class="btn btn-primary">Enquire</a>
  </div>
</section>
"""
    write("events.html", page(
        "events.html", "Events",
        "Upcoming events at The Empire Studio's East London live room, from candlelit concerts to "
        "ticketed live sessions.",
        body,
        keywords="recording studio east london, live room london, events, live music east london",
        og_image=img('33a_Wadeson_Street-11'),
    ))


SITEMAP_PAGES = [
    ("", "1.0", "weekly"),
    ("about-us.html", "0.8", "monthly"),
    ("equipment.html", "0.8", "monthly"),
    ("testimonials.html", "0.7", "monthly"),
    ("gallery.html", "0.7", "monthly"),
    ("news.html", "0.6", "weekly"),
    ("contact.html", "0.9", "monthly"),
    ("events.html", "0.6", "weekly"),
]


def build_sitemap():
    from build import SITE_URL
    import datetime
    today = datetime.date.today().isoformat()
    urls = "\n".join(
        f"  <url>\n"
        f"    <loc>{SITE_URL}/{path}</loc>\n"
        f"    <lastmod>{today}</lastmod>\n"
        f"    <changefreq>{freq}</changefreq>\n"
        f"    <priority>{priority}</priority>\n"
        f"  </url>"
        for path, priority, freq in SITEMAP_PAGES
    )
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
"""
    write("sitemap.xml", xml)


def build_robots():
    from build import SITE_URL
    txt = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    write("robots.txt", txt)


if __name__ == "__main__":
    build_home()
    build_about()
    build_equipment()
    build_testimonials()
    build_gallery()
    build_news()
    build_contact()
    build_events()
    build_sitemap()
    build_robots()
