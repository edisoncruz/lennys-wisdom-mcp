#!/usr/bin/env python3
"""
Episode Metadata Extractor for Lenny's Wisdom MCP

This script extracts structured metadata from podcast transcripts.

Usage:
    # Manual mode (outputs prompt for Claude in Cowork)
    python extract_episode_metadata.py --transcript "Brian Chesky.txt" --manual

    # API mode (requires ANTHROPIC_API_KEY)
    python extract_episode_metadata.py --transcript "Brian Chesky.txt" --api
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional
import argparse

# Optional: Only needed for API mode
try:
    from anthropic import Anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False


def load_transcript(transcript_path: Path) -> str:
    """Load transcript file"""
    with open(transcript_path, 'r', encoding='utf-8') as f:
        return f.read()


def create_extraction_prompt(transcript_text: str, guest_name: str) -> str:
    """Create the extraction prompt for Claude"""

    # Truncate if too long (for display in manual mode)
    if len(transcript_text) > 50000:
        transcript_preview = transcript_text[:50000] + "\n\n[... transcript continues ...]"
    else:
        transcript_preview = transcript_text

    prompt = f"""Extract structured metadata from this Lenny's Podcast transcript.

TRANSCRIPT:
{transcript_preview}

EXTRACTION TASK:

Extract the following information and return as valid JSON:

1. **Guest Information**:
   - Full name: {guest_name}
   - Title (their role, e.g., "CEO and Co-founder")
   - Company name
   - Brief bio (2-3 sentences about their background and expertise)

2. **Episode Summary**:
   - 2-3 sentences covering the main themes discussed

3. **Topics**:
   - List 3-8 topic tags from this controlled vocabulary:
     leadership, founder-mode, product-management, hiring, firing, feedback,
     culture, scaling, growth-marketing, metrics, decision-making, strategy,
     team-building, performance-management, communication, sales, fundraising,
     customer-research, design, engineering-management, remote-work, AI-ML,
     career-development, personal-productivity, mental-health
   - Pick the most relevant, don't force all topics

4. **Key Themes** (2-4 major themes):
   For each theme:
   - Theme name (concise, 3-6 words)
   - Description (one sentence explaining the theme)
   - Relevance score (0.0 to 1.0, how central is this theme?)

5. **Key Insights** (8-15 insights):
   For each insight:
   - Quote: The actual quote (verbatim from transcript)
   - Timestamp: Approximate timestamp (look for speaker timestamps)
   - Context: What was being discussed (2-3 sentences)
   - Insight: The principle/takeaway (1 sentence)
   - Topics: 1-3 relevant topic tags
   - Actionable: true/false (can someone apply this?)

OUTPUT FORMAT (valid JSON):

{{
  "guest_name": "Full Name",
  "guest_title": "Title and Role",
  "guest_company": "Company",
  "guest_bio": "2-3 sentence bio...",
  "episode_summary": "2-3 sentence summary...",
  "topics": ["topic1", "topic2", "topic3"],
  "key_themes": [
    {{
      "theme": "Theme Name",
      "description": "One sentence description",
      "relevance_score": 0.95
    }}
  ],
  "key_insights": [
    {{
      "quote": "Exact quote from transcript...",
      "timestamp": "32:15",
      "context": "What was being discussed...",
      "insight": "The key takeaway...",
      "topics": ["topic1", "topic2"],
      "actionable": true
    }}
  ]
}}

Return ONLY valid JSON, no additional text before or after.
"""
    return prompt


def extract_via_api(transcript_text: str, guest_name: str, api_key: str) -> dict:
    """Extract metadata using Anthropic API"""
    if not HAS_ANTHROPIC:
        raise ImportError("anthropic library not installed. Run: pip install anthropic")

    client = Anthropic(api_key=api_key)
    prompt = create_extraction_prompt(transcript_text, guest_name)

    print(f"🤖 Calling Claude API to extract metadata for {guest_name}...")

    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=4096,
        temperature=0,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    response_text = message.content[0].text

    # Parse JSON response
    try:
        # Find JSON in response (in case there's extra text)
        json_start = response_text.find('{')
        json_end = response_text.rfind('}') + 1
        json_text = response_text[json_start:json_end]

        data = json.loads(json_text)
        return data
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON response: {e}")
        print(f"Response was:\n{response_text}")
        sys.exit(1)


def extract_manual(transcript_text: str, guest_name: str) -> None:
    """Output prompt for manual extraction via Claude in Cowork"""
    prompt = create_extraction_prompt(transcript_text, guest_name)

    print("=" * 80)
    print("MANUAL EXTRACTION MODE")
    print("=" * 80)
    print()
    print("Copy the prompt below and paste it to Claude in Cowork mode.")
    print("Then copy Claude's JSON response and paste it back here.")
    print()
    print("=" * 80)
    print("PROMPT START")
    print("=" * 80)
    print()
    print(prompt)
    print()
    print("=" * 80)
    print("PROMPT END")
    print("=" * 80)
    print()
    print("Paste Claude's JSON response below (then press Enter, then Ctrl+D):")
    print()

    # Read response from stdin
    response_lines = []
    try:
        while True:
            line = input()
            response_lines.append(line)
    except EOFError:
        pass

    response_text = '\n'.join(response_lines)

    # Parse JSON
    try:
        json_start = response_text.find('{')
        json_end = response_text.rfind('}') + 1
        json_text = response_text[json_start:json_end]

        data = json.loads(json_text)
        return data
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON: {e}")
        sys.exit(1)


def create_episode_json(extracted_data: dict, guest_name: str, transcript_path: Path) -> dict:
    """Create full episode JSON from extracted data"""

    # Generate episode ID
    guest_slug = guest_name.lower().replace(' ', '-').replace("'", "")
    episode_id = f"ep-{guest_slug}"

    # Count words in transcript
    with open(transcript_path, 'r') as f:
        word_count = len(f.read().split())

    # Build episode JSON
    episode = {
        "id": episode_id,
        "guest_id": f"guest-{guest_slug}",
        "guest_name": extracted_data["guest_name"],
        "title": f"{extracted_data['guest_name']} on Lenny's Podcast",  # Can be refined
        "description": extracted_data.get("episode_summary", ""),
        "summary": extracted_data["episode_summary"],
        "topics": extracted_data["topics"],
        "key_themes": extracted_data["key_themes"],
        "key_insights": [],
        "frameworks_mentioned": [],  # To be filled by framework extractor
        "situations_addressed": [],  # To be filled later
        "quotes_extracted": len(extracted_data["key_insights"]),
        "transcript_available": True,
        "transcript_path": f"transcripts/{transcript_path.name}",
        "transcript_word_count": word_count,
        "extraction_metadata": {
            "extracted_at": datetime.utcnow().isoformat() + "Z",
            "extraction_version": "1.0",
            "llm_model": "claude-sonnet-4.5",
            "human_reviewed": False
        }
    }

    # Convert key_insights to proper format
    for idx, insight in enumerate(extracted_data["key_insights"], 1):
        insight_id = f"insight-{episode_id}-{idx:03d}"
        episode["key_insights"].append({
            "id": insight_id,
            "insight": insight["insight"],
            "quote": insight["quote"],
            "timestamp": insight.get("timestamp", "unknown"),
            "context": insight["context"],
            "topics": insight["topics"],
            "actionable": insight.get("actionable", True)
        })

    return episode


def main():
    parser = argparse.ArgumentParser(description="Extract episode metadata from transcripts")
    parser.add_argument("--transcript", required=True, help="Path to transcript file")
    parser.add_argument("--manual", action="store_true", help="Manual mode (use Claude in Cowork)")
    parser.add_argument("--api", action="store_true", help="API mode (use Anthropic API)")
    parser.add_argument("--output-dir", default="output", help="Output directory for JSON files")

    args = parser.parse_args()

    # Validate mode
    if not args.manual and not args.api:
        print("❌ Error: Must specify either --manual or --api mode")
        sys.exit(1)

    if args.manual and args.api:
        print("❌ Error: Cannot use both --manual and --api")
        sys.exit(1)

    # Load transcript
    transcript_path = Path(args.transcript)
    if not transcript_path.exists():
        print(f"❌ Error: Transcript not found: {transcript_path}")
        sys.exit(1)

    guest_name = transcript_path.stem  # Filename without extension
    print(f"📄 Loading transcript: {guest_name}")

    transcript_text = load_transcript(transcript_path)
    print(f"✓ Loaded transcript ({len(transcript_text)} characters, {len(transcript_text.split())} words)")

    # Extract metadata
    if args.api:
        import os
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            print("❌ Error: ANTHROPIC_API_KEY environment variable not set")
            sys.exit(1)

        extracted_data = extract_via_api(transcript_text, guest_name, api_key)
    else:
        extracted_data = extract_manual(transcript_text, guest_name)

    print(f"✓ Extracted metadata successfully")

    # Create episode JSON
    episode = create_episode_json(extracted_data, guest_name, transcript_path)

    # Save to file
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{episode['id']}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(episode, f, indent=2, ensure_ascii=False)

    print(f"✓ Saved episode JSON to: {output_file}")
    print()
    print("Summary:")
    print(f"  - Guest: {episode['guest_name']}")
    print(f"  - Topics: {', '.join(episode['topics'])}")
    print(f"  - Themes: {len(episode['key_themes'])}")
    print(f"  - Insights: {len(episode['key_insights'])}")


if __name__ == "__main__":
    main()
