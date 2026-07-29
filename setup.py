from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="forbes-story-angle-generator",
    version="1.0.0",
    author="ForbesPlacement.com",
    author_email="info@forbesplacement.com",
    description="Forbes Story Angle Generator is an AI-powered platform that helps businesses, founders, executives, and marketing teams develop compelling editorial story ideas for premium business publications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://forbesplacement.com",
    project_urls={
        "Homepage": "https://forbesplacement.com",
        "GitHub": "https://github.com/forbes-placement/forbes-story-angle-generator",
        "Documentation": "https://forbes-story-angle-generator.readthedocs.io",
        "PyPI": "https://pypi.org/project/forbes-story-angle-generator",
    },
    py_modules=["angle_generator"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=[
        "forbes-story-angle",
        "editorial-placement",
        "pr-strategy",
        "thought-leadership",
        "brand-authority",
        "media-visibility",
        "forbesplacement",
    ],
    entry_points={
        "console_scripts": [
            "forbes-story-angle=angle_generator:main",
        ],
    },
)
