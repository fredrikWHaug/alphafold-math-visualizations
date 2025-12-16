# Manim Visualizations

A simple setup for creating mathematical animations with Manim.

## Setup (macOS)

Install system dependencies:

```bash
brew install cairo pkg-config ffmpeg
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Note: Adapt the activation command for your shell if needed (e.g., `activate.fish` for Fish shell).

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Render a scene:

```bash
python -m manim -pql --progress_bar display scene.py SimpleCircle
```

Output will be saved to `media/videos/scene/480p15/`

## Flags

- `-p` - Preview the animation when done
- `-ql` - Low quality (fast rendering)
- `-qh` - High quality (slower rendering)
- `--progress_bar display` - Show rendering progress
