# DoomXP — Windows XP Interactive Portfolio Template

A high-fidelity, interactive Windows XP-themed portfolio template built with Next.js, React, and Tailwind CSS. Themed after **Doctor Doom (Victor Von Doom)** and Marvel Studios' upcoming **Avengers: Doomsday** and **Avengers: Secret Wars**, this template can be used out of the box or customized into your own personal developer portfolio.

---

## Live Demo & Theming
- **Theme**: Victor Von Doom • Supreme Monarch of Latveria
- **Default Background**: Live Official *Avengers: Doomsday* Multiverse Countdown Clock
- **Easter Egg**: Multi-user login screen with Reed Richards ("Access Denied" critical error)

---

## Features

### 1. Authentic Windows XP Experience
- **Boot Sequence**: Classic Windows XP boot sequence with stylized sovereign green and gold flags, progress loading bar, and fluid transition.
- **Multi-User Login Screen**:
  - Choose between **Victor Von Doom** and **Reed Richards**.
  - Logging in as Victor Von Doom launches the desktop.
  - Attempting to log in as Reed Richards triggers an authentic Windows XP Critical Stop Dialog with custom audio: *"ACCESS DENIED: REED RICHARDS. Richards, your pathetic intellect has no authority in Latveria."*
- **Window Management**:
  - Draggable, resizable, minimizable, and maximizable windows.
  - Active z-index stacking and taskbar grouping.
  - Classic Luna Blue gradient title bars and vintage XP minimize/maximize/close controls.

### 2. Live Multiverse Countdown Wallpaper
- Streams the official **Avengers: Doomsday Clock** (`f17J3AXVK5w`) directly in the desktop background.
- Integrated **Display Properties** control center allowing instant switching between:
  - Live Doomsday Clock Video Stream
  - Doctor Doom Sovereign Throne
  - Battleworld Incursion Sky
  - Castle Doom Twilight
  - Latverian Aurora

### 3. Applications & Windows
- **`About Victor Von Doom` (`My Computer`)**: Developer bio, sovereign titles, diplomatic channels, and key highlights.
- **`Doom_Resume.doc`**: Interactive curriculum vitae with experience, honors, credentials, and an instant **Download PDF** button.
- **`Latverian Sovereign Arsenal` (`My Projects`)**: Interactive grid of projects with custom sci-fi cover cards, tech tags, descriptions, and live demo / source code links.
- **`Avengers_Doomsday_Special_Look.mp4`**: Built-in Windows Media Player streaming the official trailer and countdown.
- **`Skills & Tools`**: Categorized tech stack covering quantum physics, robotics, arcane sorcery, and incursion defense.
- **`Imperial Honors & Royal Decrees`**: Awards, hackathons, and certifications.
- **`Recycle Bin`**: Themed trash can featuring discarded rival technology (broken Vibranium shields, Reed Richards' failed calculations).
- **`Secret Wars Badge`**: Floating aesthetic badge in the top-right corner celebrating Marvel Studios' *Avengers: Secret Wars*.

---

## Quick Start (Running Locally)

### Prerequisites
- Node.js (v18 or higher recommended)
- Or Python 3 (built-in zero-dependency fallback server)

### Installation
```bash
# Clone the repository
git clone https://github.com/<your-username>/doomxp-portfolio.git
cd doomxp-portfolio

# Start the Node.js server
npm start
# or
node server.js
```

Or run via Python:
```bash
python server.py
```

The app will launch at **http://localhost:3005** (or the next available port if 3005 is busy).

---

## How to Customize for Your Own Portfolio

This template is designed to be easily modified for your own personal developer brand:

### 1. Replace Your Profile Picture & Assets
Replace the files in the `/assets/` directory:
- `assets/profile.jpg` $\rightarrow$ Your profile picture or custom avatar.
- `assets/reed.jpg` $\rightarrow$ Any rival or secondary character for the login easter egg.
- `assets/Doom_Resume.pdf` $\rightarrow$ Your personal resume PDF for the download button.
- `assets/wall1.jpg`, `wall2.jpg`, `wall3.jpg`, `wall4.jpg` $\rightarrow$ Custom wallpapers of your choice.

### 2. Customize Your Information
Open `_next/static/immutable/chunks/42ik_u_0tp9fp.js` (or edit the component definitions):
- **Name & Title**: Search for `"Victor Von Doom"` and `"Supreme Monarch of Latveria"` and replace with your name and job title (e.g. `"Full Stack Engineer"`).
- **Location & Email**: Search for `Castle Doom, Latveria` and `doom@latveria.gov` to update your contact details.
- **Projects**: Search for `nn=[` to update the list of featured projects, live demos, descriptions, and GitHub links.
- **Skills**: Search for `nc=[` to customize your languages, frameworks, developer tools, and cloud platforms.
- **Resume Experience**: Search for `nl=[` to update your work history, company names, and bullet points.

### 3. Change Background Video
To change the desktop YouTube wallpaper, search for the YouTube ID `f17J3AXVK5w` and replace it with any YouTube video ID of your choice.

---

## Deployment

### Deploying to Vercel
Deploy to Vercel with a single command:
```bash
vercel --prod
```

### Deploying to Netlify / GitHub Pages / Static Hosts
Since the project is self-contained with static HTML and optimized chunks, you can drag and drop the folder directly into Netlify, Vercel, or host on GitHub Pages without complex build steps.

---

## License
MIT License. Free to use, adapt, and share for personal portfolios and creative web projects.
