from __future__ import annotations

import base64
from pathlib import Path

import gradio as gr

ROOT = Path(__file__).resolve().parent
LOGO_PATH = ROOT / "assets" / "lamgo_logo.png"


def logo_data_uri() -> str:
    """Load the supplied LamGo logo as an embedded image."""
    if not LOGO_PATH.exists():
        return ""
    encoded = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


LOGO = logo_data_uri()

CSS = """
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
  --ocean-950: #03131d;
  --ocean-900: #061e2b;
  --ocean-850: #082a39;
  --ocean-800: #0b3545;
  --ocean-700: #105064;
  --teal-500: #21b6ad;
  --teal-300: #73ded0;
  --ice: #e8f6f5;
  --muted: #a8c3ca;
  --line: rgba(142, 207, 211, .16);
}
html, body, .gradio-container {
  background: var(--ocean-950) !important;
  color: var(--ice) !important;
  font-family: 'DM Sans', sans-serif !important;
}
.gradio-container {
  max-width: 1440px !important;
  padding: 22px 28px 36px !important;
}
footer { display: none !important; }
#lamgo-shell { max-width: 1280px; margin: 0 auto; }
.topbar {
  display:flex; align-items:center; justify-content:space-between; gap:24px;
  padding: 16px 22px; border:1px solid var(--line); border-radius:18px;
  background:rgba(7, 34, 47, .88); backdrop-filter:blur(16px);
  box-shadow:0 12px 40px rgba(0,0,0,.22); margin-bottom:22px;
}
.brand { display:flex; align-items:center; gap:16px; min-width:0; }
.brand img { width:76px; height:76px; object-fit:contain; filter:drop-shadow(0 5px 18px rgba(33,182,173,.14)); }
.brand-copy { min-width:0; }
.brand-name { font:800 23px 'Manrope',sans-serif; letter-spacing:.12em; color:#f0ffff; }
.brand-tag { color:var(--muted); font-size:12px; letter-spacing:.13em; text-transform:uppercase; margin-top:3px; }
.status { color:#a4e8de; border:1px solid rgba(115,222,208,.28); background:rgba(33,182,173,.08);
  padding:9px 13px; border-radius:999px; font-size:11px; letter-spacing:.12em; text-transform:uppercase; white-space:nowrap; }
.hero {
  position:relative; overflow:hidden; padding:66px 58px; border-radius:26px;
  border:1px solid rgba(115,222,208,.18);
  background: radial-gradient(ellipse at 85% 12%, rgba(33,182,173,.23), transparent 34%),
              radial-gradient(ellipse at 4% 100%, rgba(20,104,128,.34), transparent 42%),
              linear-gradient(120deg, #082536 0%, #0a3a4a 55%, #06202d 100%);
  box-shadow:0 25px 70px rgba(0,0,0,.28); margin-bottom:26px;
}
.hero:before, .hero:after {
  content:""; position:absolute; border:1px solid rgba(115,222,208,.12); border-radius:50%;
  width:390px; height:390px; right:-90px; top:-185px; animation:float 12s ease-in-out infinite;
}
.hero:after { width:510px; height:510px; right:-145px; top:-245px; animation-delay:-5s; }
.hero-content { position:relative; z-index:1; max-width:760px; }
.eyebrow { color:var(--teal-300); text-transform:uppercase; letter-spacing:.2em; font-size:11px; font-weight:700; }
.hero h1 { font:800 clamp(36px,5vw,62px)/1.06 'Manrope',sans-serif; margin:17px 0 16px; color:#f3ffff; }
.hero p { color:#c1d9dd; font-size:17px; line-height:1.8; max-width:680px; margin:0; }
.hero-rule { width:68px; height:3px; background:linear-gradient(90deg,var(--teal-500),transparent); margin:25px 0; }
.section-heading { color:#efffff; font:700 25px 'Manrope',sans-serif; margin:26px 0 8px; }
.section-sub { color:var(--muted); margin:0 0 16px; font-size:14px; }
.metric-grid { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px; margin:20px 0 28px; }
.metric {
  background:linear-gradient(145deg,rgba(14,58,73,.92),rgba(7,34,47,.92));
  border:1px solid var(--line); border-radius:17px; padding:19px 20px;
  transition:transform .25s ease,border-color .25s ease,box-shadow .25s ease;
}
.metric:hover { transform:translateY(-4px); border-color:rgba(115,222,208,.42); box-shadow:0 14px 32px rgba(0,0,0,.2); }
.metric-value { color:var(--teal-300); font:800 25px 'Manrope',sans-serif; }
.metric-label { color:var(--muted); font-size:12px; margin-top:5px; letter-spacing:.04em; }
.card-grid { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:15px; }
.info-card {
  background:linear-gradient(145deg,rgba(11,48,63,.96),rgba(6,29,42,.96));
  border:1px solid var(--line); border-radius:17px; padding:23px;
  transition:transform .25s ease,border-color .25s ease,background .25s ease;
}
.info-card:hover { transform:translateY(-3px); border-color:rgba(115,222,208,.4); background:linear-gradient(145deg,#104354,#082a3a); }
.card-kicker { color:var(--teal-300); font-size:10px; font-weight:700; letter-spacing:.17em; text-transform:uppercase; }
.info-card h3 { color:#f0ffff; font:700 17px 'Manrope',sans-serif; margin:9px 0; }
.info-card p { color:#b5cdd2; font-size:13px; line-height:1.75; margin:0; }
.icon-frame { width:39px; height:39px; display:grid; place-items:center; border-radius:12px;
  background:rgba(33,182,173,.10); border:1px solid rgba(115,222,208,.2); color:var(--teal-300); }
.icon-frame svg { width:20px; height:20px; stroke:currentColor; fill:none; stroke-width:1.7; stroke-linecap:round; stroke-linejoin:round; }
.flow { display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:10px; margin-top:16px; }
.flow-step { border:1px solid var(--line); background:rgba(9,43,57,.8); padding:17px; border-radius:14px; }
.flow-num { color:var(--teal-300); font:800 11px 'Manrope',sans-serif; letter-spacing:.15em; }
.flow-step h4 { color:#efffff; font:700 13px 'Manrope',sans-serif; margin:9px 0 5px; }
.flow-step p { color:var(--muted); font-size:11px; line-height:1.6; margin:0; }
.footer { text-align:center; color:#7899a3; font-size:11px; padding:28px 10px 8px; letter-spacing:.05em; }
.gradio-tabs { border:1px solid var(--line) !important; border-radius:18px !important; background:rgba(5,27,39,.72) !important; padding:12px !important; }
button[role="tab"] { color:#a9c5cc !important; border-radius:10px !important; border:1px solid transparent !important; }
button[role="tab"][aria-selected="true"] { color:#eaffff !important; background:rgba(33,182,173,.13) !important; border-color:rgba(115,222,208,.24) !important; }
label, .prose, .markdown { color:var(--ice) !important; }
input, textarea, select { background:#082a39 !important; color:#efffff !important; border-color:var(--line) !important; }
.dataframe { background:#082a39 !important; }
@keyframes float { 0%,100% { transform:translate3d(0,0,0) rotate(0deg); } 50% { transform:translate3d(-16px,18px,0) rotate(5deg); } }
@media (max-width:800px) {
  .gradio-container { padding:12px !important; }
  .hero { padding:42px 25px; }
  .metric-grid { grid-template-columns:repeat(2,minmax(0,1fr)); }
  .card-grid, .flow { grid-template-columns:1fr; }
  .status { display:none; }
}
"""

def icon_svg(kind: str) -> str:
    paths = {
        "shield": '<path d="M12 3 20 6v5c0 5-3.4 8.5-8 10-4.6-1.5-8-5-8-10V6l8-3Z"/><path d="m8.5 12 2.2 2.2 4.8-5"/>',
        "search": '<circle cx="10.8" cy="10.8" r="6.8"/><path d="m16 16 4.5 4.5"/>',
        "map": '<path d="m3 6 6-3 6 3 6-3v15l-6 3-6-3-6 3V6Z"/><path d="M9 3v15m6-12v15"/>',
        "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="10" cy="7" r="4"/><path d="M20 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
        "star": '<path d="m12 3 2.7 5.5 6.1.9-4.4 4.3 1 6.1-5.4-2.9-5.4 2.9 1-6.1-4.4-4.3 6.1-.9L12 3Z"/>',
        "pin": '<path d="M20 10c0 5-8 11-8 11S4 15 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/>',
    }
    return f'<div class="icon-frame"><svg viewBox="0 0 24 24" aria-hidden="true">{paths[kind]}</svg></div>'

def card(kind, kicker, title, description):
    return f"""
    <article class="info-card">
      {icon_svg(kind)}
      <div class="card-kicker">{kicker}</div>
      <h3>{title}</h3>
      <p>{description}</p>
    </article>
    """

def home_page():
    return f"""
    <div class="hero">
      <div class="hero-content">
        <div class="eyebrow">A smarter way to explore</div>
        <h1>Discover Bhutan.<br>Find your own way.</h1>
        <div class="hero-rule"></div>
        <p>LamGo brings destination discovery, traveller insights and local experiences together in one considered travel platform.</p>
      </div>
    </div>
    <div class="metric-grid">
      <div class="metric"><div class="metric-value">76</div><div class="metric-label">Destinations</div></div>
      <div class="metric"><div class="metric-value">3</div><div class="metric-label">Main categories</div></div>
      <div class="metric"><div class="metric-value">SQLite</div><div class="metric-label">Structured data store</div></div>
      <div class="metric"><div class="metric-value">Python</div><div class="metric-label">Application foundation</div></div>
    </div>
    <div class="section-heading">Welcome to LamGo</div>
    <p class="section-sub">A unified view of places, people and experiences across Bhutan.</p>
    <div class="card-grid">
      {card("map","DISCOVER","Explore with context","Browse destinations by district and category, and review useful information before you travel.")}
      {card("users","CONNECT","Learn from travellers","Discover community posts, ratings, reviews and shared travel experiences.")}
    </div>
    """

def about_page():
    return f"""
    <div class="section-heading">About the project</div>
    <p class="section-sub">The purpose, challenge and approach behind LamGo.</p>
    <div class="card-grid">
      {card("map","THE PLATFORM","What is LamGo?","LamGo is a Python Tkinter travel-discovery application designed to make it easier to explore destinations across Bhutan.")}
      {card("search","THE CHALLENGE","Information is scattered","Destination information and recommendations can be spread across different sources, making relevant places harder to discover.")}
      {card("star","THE APPROACH","A more organised discovery experience","LamGo brings destination details, images, ratings, reviews and traveller experiences into one application.")}
      {card("shield","THE GOAL","Useful and accessible discovery","The project aims to make exploring places more structured, relevant and approachable for travellers.")}
    </div>
    """

def features_page():
    items = [
        ("shield","01 / ACCOUNT","User authentication","Create accounts, log in and manage user profiles."),
        ("search","02 / DISCOVERY","Smart search","Find destinations using keywords, districts and categories."),
        ("map","03 / DESTINATIONS","Destination discovery","Browse place details, photographs, ratings and information."),
        ("users","04 / COMMUNITY","Community interaction","Share posts, like content and interact with other travellers."),
        ("star","05 / FEEDBACK","Reviews and ratings","Share experiences and provide feedback about destinations."),
        ("pin","06 / LOCATION","Location support","Use approximate location information or select a location manually."),
    ]
    return '<div class="section-heading">Platform capabilities</div><p class="section-sub">The core functions described in the LamGo project.</p><div class="card-grid">' + "".join(card(*x) for x in items) + '</div>'

def technology_page():
    items = [
        ("PYTHON","Application logic","The main programming language used by the application."),
        ("TKINTER","Desktop interface","Creates the graphical interface and application pages."),
        ("SQLITE","Structured storage","Stores destination information in a local relational database."),
        ("PILLOW","Image processing","Supports image loading and image processing."),
        ("JSON","Local data","Stores local account, social and user activity information."),
    ]
    return '<div class="section-heading">Technology stack</div><p class="section-sub">The tools and technologies identified in the project.</p><div class="card-grid">' + "".join(card("shield","TECHNOLOGY",x[0],x[2]) for x in items) + '</div>'

def architecture_page():
    return """
    <div class="section-heading">System architecture</div>
    <p class="section-sub">A three-layer view of how the application is organised.</p>
    <div class="card-grid">
      <article class="info-card"><div class="card-kicker">LAYER 01</div><h3>Presentation layer</h3><p>Tkinter pages provide the visual interface through which users interact with LamGo.</p></article>
      <article class="info-card"><div class="card-kicker">LAYER 02</div><h3>Application logic</h3><p>The main application controller and supporting modules manage navigation, user actions, recommendations and application state.</p></article>
      <article class="info-card"><div class="card-kicker">LAYER 03</div><h3>Data layer</h3><p>SQLite stores destination information, while JSON files support local accounts, community activity and user interactions.</p></article>
    </div>
    <div class="info-card" style="margin-top:15px;text-align:center">
      <div class="card-kicker">DATA FLOW</div><h3>User → Tkinter Interface → Application Logic → SQLite / JSON</h3>
    </div>
    """

def database_page():
    data = [
        ["id","INTEGER","Primary key for each destination"],
        ["name","TEXT","Name of the destination"],
        ["district","TEXT","District where the place is located"],
        ["category","TEXT","Type of destination"],
        ["rating","REAL","Average destination rating"],
        ["reviews","INTEGER","Number of traveller reviews"],
        ["description","TEXT","Detailed destination information"],
        ["latitude","REAL","Geographical latitude"],
        ["longitude","REAL","Geographical longitude"],
        ["image","TEXT","Destination image path"],
    ]
    return data

def recommendation_page(choice):
    descriptions = {
        "Search Match": "Matches destinations with keywords entered by the traveller.",
        "User Interests": "Uses user interests to support more relevant destination suggestions.",
        "Recent Activity": "Recent searches and interactions can help improve future discovery.",
        "Location": "Location information can help prioritise relevant destinations.",
        "Ratings": "Ratings and reviews can help highlight popular destinations.",
    }
    return f"""
    <div class="info-card" style="margin-top:15px">
      <div class="card-kicker">SELECTED DISCOVERY SIGNAL</div>
      <h3>{choice}</h3><p>{descriptions[choice]}</p>
    </div>
    """

def flow_page():
    steps = [
        ("01","Authenticate","Create an account or log in."),
        ("02","Explore","Browse by category, district or search."),
        ("03","Discover","Review destination information and images."),
        ("04","Interact","Save places and share experiences."),
        ("05","Personalise","Use interests and activity to guide discovery."),
    ]
    return '<div class="section-heading">Application journey</div><p class="section-sub">A typical traveller journey through LamGo.</p><div class="flow">' + "".join(
        f'<div class="flow-step"><div class="flow-num">{n}</div><h4>{title}</h4><p>{desc}</p></div>' for n,title,desc in steps
    ) + '</div>'

def future_page():
    items = [
        ("Cloud backend","Add secure cloud services for cross-device accounts and community activity."),
        ("Mobile experience","Develop a web or mobile version with device location permissions."),
        ("Relational data","Move user, post, comment and notification information into a relational database."),
        ("Maps and routes","Add online maps, route planning and travel itinerary features."),
        ("Security","Improve security with stronger production authentication methods."),
    ]
    return '<div class="section-heading">Future enhancements</div><p class="section-sub">Potential next steps identified for the project.</p><div class="card-grid">' + "".join(card("star","ROADMAP",*x) for x in items) + '</div>'

header = f"""
<div class="topbar">
  <div class="brand">
    {'<img src="' + LOGO + '" alt="LamGo logo">' if LOGO else ''}
    <div class="brand-copy">
      <div class="brand-name">LAMGO</div>
      <div class="brand-tag">Discover Bhutan · Project showcase</div>
    </div>
  </div>
  <div class="status">Travel discovery platform</div>
</div>
"""

with gr.Blocks(title="LamGo | Discover Bhutan", css=CSS, theme=gr.themes.Base(
    primary_hue="teal", secondary_hue="cyan", neutral_hue="slate"
)) as demo:
    with gr.Column(elem_id="lamgo-shell"):
        gr.HTML(header)
        with gr.Tabs():
            with gr.Tab("Overview"):
                gr.HTML(home_page())
            with gr.Tab("About"):
                gr.HTML(about_page())
            with gr.Tab("Features"):
                gr.HTML(features_page())
            with gr.Tab("Technology"):
                gr.HTML(technology_page())
            with gr.Tab("Architecture"):
                gr.HTML(architecture_page())
            with gr.Tab("Data design"):
                gr.HTML('<div class="section-heading">Destination data model</div><p class="section-sub">The places table fields described in the project.</p>')
                gr.Dataframe(
                    headers=["Field", "Type", "Purpose"],
                    value=database_page(),
                    interactive=False,
                    wrap=True,
                )
            with gr.Tab("Smart discovery"):
                factor = gr.Radio(
                    choices=["Search Match", "User Interests", "Recent Activity", "Location", "Ratings"],
                    value="Search Match",
                    label="Choose a discovery factor",
                )
                output = gr.HTML(recommendation_page("Search Match"))
                factor.change(fn=recommendation_page, inputs=factor, outputs=output)
            with gr.Tab("Application flow"):
                gr.HTML(flow_page())
            with gr.Tab("Roadmap"):
                gr.HTML(future_page())
        gr.HTML('<div class="footer">LAMGO · DISCOVER BHUTAN &nbsp; / &nbsp; PROJECT SHOWCASE</div>')

if __name__ == "__main__":
    demo.launch()
