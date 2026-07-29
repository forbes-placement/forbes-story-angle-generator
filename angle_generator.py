#!/usr/bin/env python3
"""
Forbes Story Angle Generator
An AI-powered platform that helps businesses, founders, executives,
and marketing teams develop compelling editorial story ideas for
premium business publications.
https://forbesplacement.com
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def get_priority_action(scores: dict) -> str:
    labels = {
        "story_angle_quality": "Story Angle Quality",
        "editorial_fit": "Editorial Fit",
        "brand_authority": "Brand Authority",
        "media_attention": "Media Attention",
        "narrative_strength": "Narrative Strength",
        "seo_visibility": "SEO & Visibility",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_publication_fit(editorial: int, brand: int, narrative: int) -> dict:
    return {
        "Forbes": min(100, round((editorial + brand) / 2 * 1.02)),
        "Business Insider": min(100, round(narrative * 1.0)),
        "Entrepreneur": min(100, round((editorial + narrative) / 2)),
        "Fast Company": min(100, round(brand * 0.96)),
    }


def generate_angle(
    brand: str,
    story_type: str = "executive-profile",
    story_angle_quality: int = 88,
    editorial_fit: int = 85,
    brand_authority: int = 90,
    media_attention: int = 82,
    narrative_strength: int = 87,
    seo_visibility: int = 80,
) -> dict:
    """
    Generate and score story angles for premium editorial placement.

    Args:
        brand: Brand name or identifier
        story_type: Type of editorial story
        story_angle_quality: Story angle quality score (0-100)
        editorial_fit: Editorial fit score (0-100)
        brand_authority: Brand authority score (0-100)
        media_attention: Media attention score (0-100)
        narrative_strength: Narrative strength score (0-100)
        seo_visibility: SEO and visibility score (0-100)

    Returns:
        dict with individual signal scores, overall story score,
        and publication fit breakdown
    """
    scores = {
        "story_angle_quality": story_angle_quality,
        "editorial_fit": editorial_fit,
        "brand_authority": brand_authority,
        "media_attention": media_attention,
        "narrative_strength": narrative_strength,
        "seo_visibility": seo_visibility,
    }
    overall_story_score = round(sum(scores.values()) / 6)

    return {
        "brand": brand,
        "story_type": " ".join(w.capitalize() for w in story_type.split("-")),
        "story_angle_quality_score": story_angle_quality,
        "editorial_fit_score": editorial_fit,
        "brand_authority_score": brand_authority,
        "media_attention_score": media_attention,
        "narrative_strength_score": narrative_strength,
        "seo_visibility_score": seo_visibility,
        "overall_story_score": overall_story_score,
        "priority_action": get_priority_action(scores),
        "publication_fit": get_publication_fit(editorial_fit, brand_authority, narrative_strength),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    brand = args[0] if len(args) > 0 else "brand-name"
    story_type = args[1] if len(args) > 1 else "executive-profile"
    story_angle_quality = int(args[2]) if len(args) > 2 else 88
    editorial_fit = int(args[3]) if len(args) > 3 else 85
    brand_authority = int(args[4]) if len(args) > 4 else 90
    media_attention = int(args[5]) if len(args) > 5 else 82
    narrative_strength = int(args[6]) if len(args) > 6 else 87
    seo_visibility = int(args[7]) if len(args) > 7 else 80

    result = generate_angle(
        brand, story_type, story_angle_quality, editorial_fit,
        brand_authority, media_attention, narrative_strength, seo_visibility
    )

    print(f"Brand: {result['brand']}")
    print(f"Story Type: {result['story_type']}")
    print("=" * 45)
    print(f"Story Angle Quality Score:     {result['story_angle_quality_score']}/100  [{get_status(result['story_angle_quality_score'])}]")
    print(f"Editorial Fit Score:           {result['editorial_fit_score']}/100  [{get_status(result['editorial_fit_score'])}]")
    print(f"Brand Authority Score:         {result['brand_authority_score']}/100  [{get_status(result['brand_authority_score'])}]")
    print(f"Media Attention Score:         {result['media_attention_score']}/100  [{get_status(result['media_attention_score'])}]")
    print(f"Narrative Strength Score:      {result['narrative_strength_score']}/100  [{get_status(result['narrative_strength_score'])}]")
    print(f"SEO & Visibility Score:        {result['seo_visibility_score']}/100  [{get_status(result['seo_visibility_score'])}]")
    print("=" * 45)
    print(f"Overall Story Score:           {result['overall_story_score']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nPublication Fit:")
    for pub, score in result['publication_fit'].items():
        print(f"  {pub:<24} {score}/100")


if __name__ == "__main__":
    main()
