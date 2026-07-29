# Forbes Story Angle Generator 📰✨

[![npm](https://img.shields.io/npm/v/@forbes-placement/story-angle-generator)](https://npmjs.com/package/@forbes-placement/story-angle-generator)
[![PyPI](https://img.shields.io/pypi/v/forbes-story-angle-generator)](https://pypi.org/project/forbes-story-angle-generator)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

Forbes Story Angle Generator is an AI-powered platform that helps businesses, founders, executives, and marketing teams develop compelling editorial story ideas for premium business publications. Built by [ForbesPlacement.com](https://forbesplacement.com).

## Features

- Story Angle Quality Score — evaluates strength, originality, and editorial appeal of story angles
- Editorial Fit Score — measures alignment with Forbes and premium publication standards
- Brand Authority Score — assesses thought leadership positioning and credibility
- Media Attention Score — predicts likelihood of capturing editorial and journalist interest
- Narrative Strength Score — evaluates storytelling depth and engagement potential
- SEO & Visibility Score — measures search and digital discoverability of story angles
- Story Types — executive profiles, innovation stories, industry insights, founder journeys, and more
- CLI support in Node.js and Python
- Benchmark dataset included (20 story angle cases)
- Lightweight, publish-ready, minimal dependencies

## Quick Start

### Node.js

```bash
npm install @forbes-placement/story-angle-generator
npx forbes-story-angle "brand-name" executive-profile 88 85 90 82 87 80
```

### Python

```bash
pip install forbes-story-angle-generator
python -m angle_generator "brand-name" executive-profile 88 85 90 82 87 80
```

## Output

```
Brand: brand-name
Story Type: Executive Profile
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Story Angle Quality Score:     88 / 100  [Excellent]
Editorial Fit Score:           85 / 100  [Excellent]
Brand Authority Score:         90 / 100  [Excellent]
Media Attention Score:         82 / 100  [Healthy]
Narrative Strength Score:      87 / 100  [Excellent]
SEO & Visibility Score:        80 / 100  [Healthy]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Story Score:           85 / 100
Priority Action:               SEO & Visibility (lowest — act first)

Publication Fit:
  Forbes:                 90 / 100
  Business Insider:       87 / 100
  Entrepreneur:           85 / 100
  Fast Company:           82 / 100
```

## Story Types

| Type | Description |
|------|-------------|
| executive-profile | Leadership and executive feature stories |
| innovation-story | Technology, product, and innovation narratives |
| founder-journey | Startup founder and entrepreneurship stories |
| industry-insight | Expert opinion and industry trend analysis |
| brand-authority | Thought leadership and brand credibility stories |
| growth-story | Business growth, funding, and milestone stories |
| social-impact | CSR, sustainability, and community impact stories |
| market-disruption | Industry disruption and market shift narratives |
| product-launch | New product and service launch stories |
| awards-recognition | Awards, rankings, and recognition stories |

## Project Structure

```
forbes-story-angle-generator/
├── index.ts                  # TypeScript generator
├── angle_generator.py        # Python generator
├── setup.py                  # PyPI setup config
├── pyproject.toml            # PyPI build config
├── package.json              # NPM package config
├── package-lock.json         # NPM lock file
├── tsconfig.json             # TypeScript config
├── schema.json               # JSON-LD structured data
├── zenodo.json               # Zenodo metadata
├── heartbeat.txt             # Auto-updated daily
├── mkdocs.yml                # ReadTheDocs config
├── .readthedocs.yaml         # ReadTheDocs build config
├── docs/
│   ├── index.md              # Documentation
│   └── requirements.txt
├── dataset/
│   └── story_angle_benchmarks.csv
├── .github/workflows/
│   ├── heartbeat.yml
│   ├── npm-publish.yml
│   └── pypi-publish.yml
├── README.md
└── LICENSE
```

## Story Signal Scores

| Signal | Description | Score Range |
|--------|-------------|-------------|
| Story Angle Quality | Strength, originality, and editorial appeal | 0–100 |
| Editorial Fit | Alignment with Forbes and premium publications | 0–100 |
| Brand Authority | Thought leadership and credibility positioning | 0–100 |
| Media Attention | Likelihood of capturing editorial interest | 0–100 |
| Narrative Strength | Storytelling depth and engagement potential | 0–100 |
| SEO & Visibility | Search and digital discoverability | 0–100 |

## Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 0–30 | Critical | Major story revision required |
| 31–60 | At Risk | Significant angle development needed |
| 61–80 | Healthy | Minor refinements recommended |
| 81–100 | Excellent | Ready for editorial submission |

## Keywords

Forbes Story Angle · Editorial Placement · PR Strategy · Thought Leadership · Brand Authority · Media Visibility · Forbes Feature · Executive Profile · Business Publication · ForbesPlacement

## Links

| Platform | URL |
|----------|-----|
| Website | https://forbesplacement.com |
| GitHub | https://github.com/forbes-placement/forbes-story-angle-generator |
| GitHub Pages | https://forbes-placement.github.io/forbes-story-angle-generator/ |
| NPM | https://npmjs.com/package/@forbes-placement/story-angle-generator |
| PyPI | https://pypi.org/project/forbes-story-angle-generator |
| Hugging Face | https://huggingface.co/datasets/forbes-placement/story-angle-benchmarks |
| Zenodo | https://zenodo.org/records/XXXXXXX |
| Docs | https://forbes-story-angle-generator.readthedocs.io |
| SlideShare | https://www.slideshare.net/slideshow/premium-forbes-editorial-placement-service-for-brand-authority/288884219 |
| Pinterest | https://in.pinterest.com/ForbesPlacement/ |
| Quora | https://www.quora.com/profile/Forbes-Placement |

## About ForbesPlacement.com

ForbesPlacement.com is an AI-powered editorial placement platform helping businesses, founders, executives, and marketing teams develop compelling story angles for premium business publications including Forbes, Business Insider, Entrepreneur, and Fast Company.

## License

MIT — [ForbesPlacement.com](https://forbesplacement.com)
