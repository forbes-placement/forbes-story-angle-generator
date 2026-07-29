#!/usr/bin/env node

interface AngleInput {
  brand: string;
  storyType: string;
  storyAngleQuality: number;
  editorialFit: number;
  brandAuthority: number;
  mediaAttention: number;
  narrativeStrength: number;
  seoVisibility: number;
}

interface AngleOutput {
  brand: string;
  storyType: string;
  storyAngleQualityScore: number;
  editorialFitScore: number;
  brandAuthorityScore: number;
  mediaAttentionScore: number;
  narrativeStrengthScore: number;
  seoVisibilityScore: number;
  overallStoryScore: number;
  priorityAction: string;
  publicationFit: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    storyAngleQuality: "Story Angle Quality",
    editorialFit: "Editorial Fit",
    brandAuthority: "Brand Authority",
    mediaAttention: "Media Attention",
    narrativeStrength: "Narrative Strength",
    seoVisibility: "SEO & Visibility",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getPublicationFit(editorial: number, brand: number, narrative: number): Record<string, number> {
  return {
    "Forbes": Math.min(100, Math.round((editorial + brand) / 2 * 1.02)),
    "Business Insider": Math.min(100, Math.round(narrative * 1.0)),
    "Entrepreneur": Math.min(100, Math.round((editorial + narrative) / 2)),
    "Fast Company": Math.min(100, Math.round(brand * 0.96)),
  };
}

export function generateAngle(input: AngleInput): AngleOutput {
  const scores = {
    storyAngleQuality: input.storyAngleQuality,
    editorialFit: input.editorialFit,
    brandAuthority: input.brandAuthority,
    mediaAttention: input.mediaAttention,
    narrativeStrength: input.narrativeStrength,
    seoVisibility: input.seoVisibility,
  };
  const overallStoryScore = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    brand: input.brand,
    storyType: input.storyType.split("-").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" "),
    storyAngleQualityScore: input.storyAngleQuality,
    editorialFitScore: input.editorialFit,
    brandAuthorityScore: input.brandAuthority,
    mediaAttentionScore: input.mediaAttention,
    narrativeStrengthScore: input.narrativeStrength,
    seoVisibilityScore: input.seoVisibility,
    overallStoryScore,
    priorityAction: getPriorityAction(scores),
    publicationFit: getPublicationFit(input.editorialFit, input.brandAuthority, input.narrativeStrength),
  };
}

const args = process.argv.slice(2);
const brand = args[0] || "brand-name";
const storyType = args[1] || "executive-profile";
const storyAngleQuality = parseInt(args[2]) || 88;
const editorialFit = parseInt(args[3]) || 85;
const brandAuthority = parseInt(args[4]) || 90;
const mediaAttention = parseInt(args[5]) || 82;
const narrativeStrength = parseInt(args[6]) || 87;
const seoVisibility = parseInt(args[7]) || 80;

const result = generateAngle({
  brand, storyType, storyAngleQuality, editorialFit,
  brandAuthority, mediaAttention, narrativeStrength, seoVisibility,
});

console.log(`Brand: ${result.brand}`);
console.log(`Story Type: ${result.storyType}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Story Angle Quality Score:     ${result.storyAngleQualityScore}/100  [${getStatus(result.storyAngleQualityScore)}]`);
console.log(`Editorial Fit Score:           ${result.editorialFitScore}/100  [${getStatus(result.editorialFitScore)}]`);
console.log(`Brand Authority Score:         ${result.brandAuthorityScore}/100  [${getStatus(result.brandAuthorityScore)}]`);
console.log(`Media Attention Score:         ${result.mediaAttentionScore}/100  [${getStatus(result.mediaAttentionScore)}]`);
console.log(`Narrative Strength Score:      ${result.narrativeStrengthScore}/100  [${getStatus(result.narrativeStrengthScore)}]`);
console.log(`SEO & Visibility Score:        ${result.seoVisibilityScore}/100  [${getStatus(result.seoVisibilityScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Story Score:           ${result.overallStoryScore}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nPublication Fit:");
Object.entries(result.publicationFit).forEach(([pub, score]) => {
  console.log(`  ${pub.padEnd(22)} ${score}/100`);
});
