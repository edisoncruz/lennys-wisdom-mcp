#!/usr/bin/env python3
"""
Lenny's Wisdom MCP Server

Provides structured access to wisdom from 20 curated Lenny's Podcast episodes.
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Any, Optional
from fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("Lenny's Wisdom")

# Path to episode data
EPISODES_DIR = Path(__file__).parent.parent / "extraction_scripts" / "output"


def load_all_episodes() -> List[Dict[str, Any]]:
    """Load all episode JSON files"""
    episodes = []
    for json_file in EPISODES_DIR.glob("ep-*.json"):
        with open(json_file, 'r') as f:
            episodes.append(json.load(f))
    return episodes


def search_episodes(
    query: str,
    episodes: List[Dict[str, Any]],
    limit: int = 10
) -> List[Dict[str, Any]]:
    """
    Search episodes for relevant insights.

    Simple keyword matching across:
    - Insight quotes and content
    - Episode titles and summaries
    - Topics and themes
    """
    query_lower = query.lower()
    results = []

    for episode in episodes:
        # Search in episode metadata
        matches_episode = (
            query_lower in episode.get('title', '').lower() or
            query_lower in episode.get('description', '').lower() or
            query_lower in episode.get('summary', '').lower()
        )

        # Search in topics
        matches_topics = any(
            query_lower in topic.lower()
            for topic in episode.get('topics', [])
        )

        # Search in themes
        matches_themes = any(
            query_lower in theme.get('theme', '').lower() or
            query_lower in theme.get('description', '').lower()
            for theme in episode.get('key_themes', [])
        )

        # Search in insights
        matching_insights = []
        for insight in episode.get('key_insights', []):
            matches_insight = (
                query_lower in insight.get('quote', '').lower() or
                query_lower in insight.get('insight', '').lower() or
                query_lower in insight.get('context', '').lower() or
                any(query_lower in topic.lower() for topic in insight.get('topics', []))
            )
            if matches_insight:
                matching_insights.append(insight)

        # If any matches, add to results
        if matches_episode or matches_topics or matches_themes or matching_insights:
            result = {
                'episode_id': episode['id'],
                'guest_name': episode['guest_name'],
                'title': episode['title'],
                'summary': episode['summary'],
                'relevance_score': len(matching_insights),  # Simple scoring
                'matching_insights': matching_insights[:3],  # Top 3 insights
                'key_themes': episode.get('key_themes', [])[:2]  # Top 2 themes
            }
            results.append(result)

    # Sort by relevance (number of matching insights)
    results.sort(key=lambda x: x['relevance_score'], reverse=True)

    return results[:limit]


@mcp.tool()
def search_wisdom(
    query: str,
    limit: int = 10
) -> str:
    """
    Search across 20 curated Lenny's Podcast episodes for wisdom on product, growth, and leadership.

    Args:
        query: Search query (e.g., "growth strategy", "hiring", "product-market fit")
        limit: Maximum number of results to return (default: 10)

    Returns:
        Formatted search results with relevant insights, quotes, and episode context
    """
    episodes = load_all_episodes()
    results = search_episodes(query, episodes, limit)

    if not results:
        return f"No results found for '{query}'. Try broader terms like 'strategy', 'growth', 'leadership', 'hiring', or 'product-management'."

    # Format results
    output = [f"# Search Results for '{query}'\n"]
    output.append(f"Found {len(results)} relevant episode(s)\n")

    for i, result in enumerate(results, 1):
        output.append(f"\n## {i}. {result['guest_name']}: {result['title']}")
        output.append(f"**Episode:** {result['episode_id']}")
        output.append(f"**Summary:** {result['summary']}\n")

        # Add key themes
        if result['key_themes']:
            output.append("**Key Themes:**")
            for theme in result['key_themes']:
                output.append(f"- {theme['theme']} (relevance: {theme['relevance_score']:.0%})")
                output.append(f"  {theme['description']}")

        # Add matching insights
        if result['matching_insights']:
            output.append(f"\n**Relevant Insights ({len(result['matching_insights'])}):**")
            for insight in result['matching_insights']:
                output.append(f"\n### {insight['id']}")
                output.append(f"> \"{insight['quote']}\"")
                output.append(f"\n**Insight:** {insight['insight']}")
                output.append(f"**Context:** {insight['context']}")
                output.append(f"**Timestamp:** {insight['timestamp']}")
                output.append(f"**Topics:** {', '.join(insight['topics'])}")
                if insight.get('actionable'):
                    output.append("✅ **Actionable**")

        output.append("\n" + "-" * 80)

    return "\n".join(output)


@mcp.tool()
def list_guests() -> str:
    """
    List all available podcast guests with brief descriptions.

    Returns:
        Formatted list of all 20 guests and their expertise areas
    """
    episodes = load_all_episodes()

    output = ["# Available Guests (20 Episodes)\n"]

    for episode in sorted(episodes, key=lambda x: x['guest_name']):
        output.append(f"**{episode['guest_name']}** ({episode['id']})")
        output.append(f"  {episode['description'][:150]}...")
        output.append(f"  Topics: {', '.join(episode['topics'][:5])}")
        output.append("")

    return "\n".join(output)


@mcp.tool()
def get_episode(episode_id: str) -> str:
    """
    Get detailed information about a specific episode.

    Args:
        episode_id: Episode identifier (e.g., "ep-brian-chesky", "ep-shreyas-doshi")

    Returns:
        Complete episode details including all insights, themes, and frameworks
    """
    episodes = load_all_episodes()
    episode = next((ep for ep in episodes if ep['id'] == episode_id), None)

    if not episode:
        available = [ep['id'] for ep in episodes]
        return f"Episode '{episode_id}' not found. Available episodes:\n" + "\n".join(available)

    output = [f"# {episode['guest_name']}: {episode['title']}\n"]
    output.append(f"**Episode ID:** {episode['id']}")
    output.append(f"**Description:** {episode['description']}")
    output.append(f"**Summary:** {episode['summary']}\n")

    # Topics
    output.append(f"**Topics:** {', '.join(episode['topics'])}\n")

    # Key Themes
    output.append(f"## Key Themes ({len(episode['key_themes'])})\n")
    for theme in episode['key_themes']:
        output.append(f"### {theme['theme']} (Relevance: {theme['relevance_score']:.0%})")
        output.append(f"{theme['description']}\n")

    # Key Insights
    output.append(f"## Key Insights ({len(episode['key_insights'])})\n")
    for i, insight in enumerate(episode['key_insights'], 1):
        output.append(f"### {i}. {insight['id']}")
        output.append(f"> \"{insight['quote']}\"")
        output.append(f"\n**Insight:** {insight['insight']}")
        output.append(f"**Context:** {insight['context']}")
        output.append(f"**Timestamp:** {insight['timestamp']}")
        output.append(f"**Topics:** {', '.join(insight['topics'])}")
        if insight.get('actionable'):
            output.append("✅ **Actionable**")
        output.append("")

    # Frameworks mentioned
    if episode.get('frameworks_mentioned'):
        output.append(f"## Frameworks Mentioned")
        output.append(f"{', '.join(episode['frameworks_mentioned'])}\n")

    # Metadata
    output.append(f"## Episode Metadata")
    output.append(f"- Transcript: {episode.get('transcript_word_count', 0):,} words")
    output.append(f"- Extracted: {episode['extraction_metadata']['extracted_at']}")
    output.append(f"- Model: {episode['extraction_metadata']['llm_model']}")

    return "\n".join(output)


@mcp.tool()
def list_frameworks() -> str:
    """
    List all frameworks and mental models mentioned across all episodes.

    This tool extracts and catalogs all named frameworks (DHM, LNO, Pre-mortems, JTBD, etc.)
    mentioned by guests, showing which episodes cover each framework.

    Returns:
        Complete catalog of frameworks with descriptions and episode references

    Examples:
        - Product Strategy: DHM Framework, Eigenquestions, Pre-mortems
        - Decision-Making: LNO Framework, High vs Low Stakes
        - Growth: Black/Blue Loops, Kindle vs Fire Strategies
        - Hiring: Reference Checks Framework, Good PM/Bad PM
    """
    episodes = load_all_episodes()

    # Collect all frameworks
    frameworks = {}
    for episode in episodes:
        if episode.get('frameworks_mentioned'):
            for framework_id in episode['frameworks_mentioned']:
                if framework_id not in frameworks:
                    frameworks[framework_id] = {
                        'episodes': [],
                        'insights': []
                    }

                frameworks[framework_id]['episodes'].append({
                    'guest': episode['guest_name'],
                    'episode_id': episode['id']
                })

                # Find insights that mention this framework
                for insight in episode.get('key_insights', []):
                    if (framework_id.lower() in insight.get('quote', '').lower() or
                        framework_id.lower() in insight.get('insight', '').lower() or
                        framework_id.lower() in insight.get('context', '').lower()):
                        frameworks[framework_id]['insights'].append({
                            'guest': episode['guest_name'],
                            'quote': insight['quote'][:200] + "..." if len(insight['quote']) > 200 else insight['quote'],
                            'insight': insight['insight']
                        })

    if not frameworks:
        return "No frameworks found in episodes."

    # Create framework names mapping (clean up IDs to readable names)
    framework_names = {
        'framework-dhm-001': 'DHM Framework (Delight, Hard-to-copy, Margin-enhancing)',
        'framework-lno-001': 'LNO Framework (Leverage, Neutral, Overhead)',
        'framework-pre-mortems-001': 'Pre-mortems (Tigers, Paper Tigers, Elephants)',
        'framework-jtbd-001': 'Jobs to Be Done (JTBD)',
        'framework-black-blue-loops-001': 'Black Loops vs Blue Loops (Growth)',
        'framework-eigenquestions-001': 'Eigenquestions',
        'framework-good-pm-bad-pm-001': 'Good Product Manager, Bad Product Manager',
        'framework-managerial-leverage-001': 'Managerial Leverage',
        'framework-personal-operating-principles-001': 'Personal Operating Principles',
        'framework-maker-billing-001': 'Maker Billing (Pricing)',
        'framework-hypothesis-based-coaching-001': 'Hypothesis-Based Coaching',
        'framework-house-architecture-001': 'House Architecture for Companies',
        'framework-explorer-not-lecturer-001': 'Explorer Not Lecturer (Management)'
    }

    output = [f"# Product Management Frameworks Catalog\n"]
    output.append(f"Found {len(frameworks)} frameworks across {len(episodes)} episodes\n")
    output.append("=" * 80 + "\n")

    for i, (framework_id, data) in enumerate(sorted(frameworks.items()), 1):
        # Get readable name or use ID
        framework_name = framework_names.get(framework_id, framework_id.replace('-', ' ').title())

        output.append(f"\n## {i}. {framework_name}")
        output.append(f"**Framework ID:** {framework_id}")
        output.append(f"**Mentioned in {len(data['episodes'])} episode(s):**")
        for ep in data['episodes']:
            output.append(f"  - **{ep['guest']}** ({ep['episode_id']})")

        # Show example insight if available
        if data['insights']:
            output.append(f"\n**Example Usage:**")
            insight = data['insights'][0]
            output.append(f"> \"{insight['quote']}\"")
            output.append(f"— {insight['guest']}\n")

        output.append("-" * 80)

    output.append(f"\n## Framework Categories\n")
    output.append("**Product Strategy:** DHM, Eigenquestions, Pre-mortems")
    output.append("**Decision-Making:** LNO, Pre-mortems, Hypothesis-Based Coaching")
    output.append("**Growth:** Black/Blue Loops, Maker Billing")
    output.append("**Leadership:** Managerial Leverage, Good PM/Bad PM, Personal Operating Principles")
    output.append("**Company Building:** House Architecture, Explorer Not Lecturer")

    return "\n".join(output)


@mcp.tool()
def get_quotes_by_guest(guest_name: str, topic: Optional[str] = None, limit: int = 10) -> str:
    """
    Get all quotes from a specific guest, optionally filtered by topic.

    This tool retrieves verbatim quotes and insights from a particular guest,
    perfect for deep-diving into a specific leader's philosophy and advice.

    Args:
        guest_name: Name of the guest (e.g., "Ben Horowitz", "Brian Chesky", "Shreyas Doshi")
        topic: Optional topic filter (e.g., "hiring", "leadership", "decision-making")
        limit: Maximum number of quotes to return (default: 10)

    Returns:
        Collection of quotes and insights from the specified guest

    Examples:
        - get_quotes_by_guest("Ben Horowitz") → All Ben quotes
        - get_quotes_by_guest("Brian Chesky", "leadership") → Brian's leadership quotes
        - get_quotes_by_guest("Deb Liu", "career") → Deb's career advice
    """
    episodes = load_all_episodes()

    # Find the guest's episode
    guest_episode = None
    for episode in episodes:
        if guest_name.lower() in episode['guest_name'].lower():
            guest_episode = episode
            break

    if not guest_episode:
        available_guests = sorted([ep['guest_name'] for ep in episodes])
        return f"Guest '{guest_name}' not found. Available guests:\n" + "\n".join(f"- {g}" for g in available_guests)

    # Get all insights
    insights = guest_episode.get('key_insights', [])

    # Filter by topic if specified
    if topic:
        topic_lower = topic.lower()
        insights = [
            insight for insight in insights
            if any(topic_lower in t.lower() for t in insight.get('topics', [])) or
               topic_lower in insight.get('quote', '').lower() or
               topic_lower in insight.get('insight', '').lower()
        ]

    if not insights:
        if topic:
            return f"No quotes found from {guest_episode['guest_name']} on topic '{topic}'. Try broader terms or remove the topic filter."
        return f"No quotes found from {guest_episode['guest_name']}."

    insights = insights[:limit]

    output = [f"# Quotes from {guest_episode['guest_name']}\n"]
    if topic:
        output.append(f"**Filtered by topic:** {topic}")
    output.append(f"**Episode:** {guest_episode['id']}")
    output.append(f"**Found:** {len(insights)} quote(s)\n")
    output.append("=" * 80 + "\n")

    for i, insight in enumerate(insights, 1):
        output.append(f"## Quote {i}")
        output.append(f"> \"{insight['quote']}\"\n")
        output.append(f"**Insight:** {insight['insight']}\n")
        output.append(f"**Context:** {insight['context']}")
        output.append(f"**Topics:** {', '.join(insight['topics'])}")
        output.append(f"**Timestamp:** {insight['timestamp']}")
        if insight.get('actionable'):
            output.append("✅ **Actionable**")
        output.append("\n" + "-" * 80 + "\n")

    return "\n".join(output)


@mcp.tool()
def compare_perspectives(topic: str, guests: Optional[List[str]] = None) -> str:
    """
    Compare how different product leaders approach the same topic.

    This tool shows side-by-side perspectives from multiple guests on a specific topic,
    revealing different approaches, frameworks, and philosophies.

    Args:
        topic: Topic to compare (e.g., "leadership", "hiring", "decision-making", "product strategy")
        guests: Optional list of specific guests to compare (e.g., ["Brian Chesky", "Ben Horowitz"])
                If not specified, shows all guests who have insights on this topic

    Returns:
        Comparative analysis showing how different leaders approach the same challenge

    Examples:
        - compare_perspectives("leadership") → All leadership perspectives
        - compare_perspectives("hiring", ["Ben Horowitz", "Shishir Mehrotra"]) → Specific comparison
        - compare_perspectives("product-market fit") → Different approaches to PMF
    """
    episodes = load_all_episodes()
    topic_lower = topic.lower()

    # Collect insights by guest
    guest_insights = {}
    for episode in episodes:
        guest_name = episode['guest_name']

        # Skip if specific guests requested and this isn't one of them
        if guests and guest_name not in guests:
            continue

        # Find matching insights
        matching_insights = []
        for insight in episode.get('key_insights', []):
            matches = (
                any(topic_lower in t.lower() for t in insight.get('topics', [])) or
                topic_lower in insight.get('quote', '').lower() or
                topic_lower in insight.get('insight', '').lower() or
                topic_lower in insight.get('context', '').lower()
            )
            if matches:
                matching_insights.append(insight)

        if matching_insights:
            guest_insights[guest_name] = {
                'episode_id': episode['id'],
                'insights': matching_insights[:3]  # Top 3 insights
            }

    if not guest_insights:
        if guests:
            return f"No insights found on '{topic}' from {', '.join(guests)}. Try broader terms or different guests."
        return f"No insights found on '{topic}'. Try broader terms like 'strategy', 'growth', 'leadership', or 'hiring'."

    output = [f"# Comparing Perspectives on: \"{topic}\"\n"]
    output.append(f"Perspectives from {len(guest_insights)} product leader(s)\n")
    output.append("=" * 80 + "\n")

    for i, (guest_name, data) in enumerate(guest_insights.items(), 1):
        output.append(f"\n## {i}. {guest_name}'s Perspective")
        output.append(f"**Episode:** {data['episode_id']}\n")

        for j, insight in enumerate(data['insights'], 1):
            output.append(f"### Insight {j}")
            output.append(f"> \"{insight['quote']}\"\n")
            output.append(f"**{guest_name}'s Take:** {insight['insight']}\n")
            output.append(f"**Context:** {insight['context']}")
            if insight.get('actionable'):
                output.append("✅ **Actionable**")
            output.append("")

        output.append("-" * 80)

    # Add synthesis section
    output.append(f"\n## Key Takeaways")
    output.append(f"These {len(guest_insights)} leaders offer different perspectives on **{topic}**:")
    for guest_name in guest_insights.keys():
        output.append(f"- **{guest_name}**: {len(guest_insights[guest_name]['insights'])} insights")

    return "\n".join(output)


@mcp.tool()
def get_actionable_insights(topic: Optional[str] = None, limit: int = 15) -> str:
    """
    Get only insights marked as immediately actionable, optionally filtered by topic.

    This tool surfaces the most practical, actionable advice from all episodes,
    filtering out theoretical content to show only what you can do RIGHT NOW.

    Args:
        topic: Optional topic to filter by (e.g., "hiring", "decision-making", "leadership")
        limit: Maximum number of insights to return (default: 15)

    Returns:
        Actionable insights with clear takeaways you can implement immediately

    Examples:
        - get_actionable_insights() → All actionable insights
        - get_actionable_insights("hiring") → Actionable hiring advice
        - get_actionable_insights("growth-marketing") → Actionable growth tactics
    """
    episodes = load_all_episodes()

    # Collect all actionable insights
    actionable_insights = []
    for episode in episodes:
        for insight in episode.get('key_insights', []):
            if insight.get('actionable'):
                # If topic filter specified, check if insight matches
                if topic:
                    topic_lower = topic.lower()
                    matches_topic = any(
                        topic_lower in t.lower()
                        for t in insight.get('topics', [])
                    )
                    if not matches_topic:
                        continue

                actionable_insights.append({
                    'guest': episode['guest_name'],
                    'episode_id': episode['id'],
                    'insight': insight
                })

    if not actionable_insights:
        if topic:
            return f"No actionable insights found for topic '{topic}'. Try broader terms or remove the topic filter."
        return "No actionable insights found."

    # Limit results
    actionable_insights = actionable_insights[:limit]

    output = []
    if topic:
        output.append(f"# Actionable Insights: {topic}\n")
    else:
        output.append(f"# Actionable Insights (All Topics)\n")

    output.append(f"Found {len(actionable_insights)} immediately actionable insights\n")
    output.append("---\n")

    for i, item in enumerate(actionable_insights, 1):
        insight = item['insight']
        output.append(f"## {i}. {item['guest']}")
        output.append(f"> \"{insight['quote']}\"\n")
        output.append(f"**✅ Action:** {insight['insight']}\n")
        output.append(f"**Context:** {insight['context']}")
        output.append(f"**Topics:** {', '.join(insight['topics'])}")
        output.append(f"**Episode:** {item['episode_id']} | **Timestamp:** {insight['timestamp']}")
        output.append("\n" + "-" * 80 + "\n")

    return "\n".join(output)


@mcp.tool()
def get_advice_for_situation(situation: str, limit: int = 10) -> str:
    """
    Get relevant advice for a specific PM situation or challenge.

    This tool searches across all episodes to find insights relevant to your situation
    and presents them as actionable advice from world-class product leaders.

    Args:
        situation: Description of your situation (e.g., "I'm joining a new company as VP Product",
                  "My team is struggling with roadmap prioritization", "I need to fire an underperformer")
        limit: Maximum number of insights to return (default: 10)

    Returns:
        Curated advice from multiple guests with specific quotes and actionable insights

    Examples:
        - "I'm starting a new role as GM of a game studio"
        - "How do I make decisions when both options seem bad?"
        - "My product has good retention but slow growth"
        - "I need to have a difficult conversation with my team"
    """
    episodes = load_all_episodes()

    # Search for relevant insights
    results = search_episodes(situation, episodes, limit=20)

    if not results:
        return f"No specific advice found for your situation. Try rephrasing or use search_wisdom() for broader results."

    # Collect all matching insights across episodes
    all_insights = []
    for result in results:
        for insight in result['matching_insights']:
            all_insights.append({
                'guest': result['guest_name'],
                'episode_id': result['episode_id'],
                'insight': insight,
                'relevance': result['relevance_score']
            })

    # Sort by actionability and relevance
    all_insights.sort(
        key=lambda x: (x['insight'].get('actionable', False), x['relevance']),
        reverse=True
    )

    output = [f"# Advice for: \"{situation}\"\n"]
    output.append(f"Found {len(all_insights[:limit])} relevant insights from {len(set(i['guest'] for i in all_insights[:limit]))} product leaders\n")
    output.append("---\n")

    for i, item in enumerate(all_insights[:limit], 1):
        insight = item['insight']
        output.append(f"## {i}. {item['guest']}'s Advice")
        output.append(f"> \"{insight['quote']}\"\n")
        output.append(f"**Actionable Insight:** {insight['insight']}\n")
        output.append(f"**Context:** {insight['context']}")
        output.append(f"**From Episode:** {item['episode_id']}")
        output.append(f"**Timestamp:** {insight['timestamp']}")
        if insight.get('actionable'):
            output.append("✅ **Immediately Actionable**")
        output.append("\n" + "-" * 80 + "\n")

    # Add summary of perspectives
    unique_guests = list(set(i['guest'] for i in all_insights[:limit]))
    output.append(f"\n**Perspectives from:** {', '.join(unique_guests)}")

    return "\n".join(output)


@mcp.tool()
def search_by_topic(topic: str, limit: int = 5) -> str:
    """
    Find episodes and insights by specific topic.

    Args:
        topic: Topic to search for (e.g., "hiring", "growth-marketing", "decision-making")
        limit: Maximum number of results

    Returns:
        Episodes and insights tagged with the specified topic
    """
    episodes = load_all_episodes()
    topic_lower = topic.lower()

    results = []
    for episode in episodes:
        # Check if topic matches episode topics
        matching_topics = [t for t in episode.get('topics', []) if topic_lower in t.lower()]

        # Get insights with this topic
        matching_insights = [
            insight for insight in episode.get('key_insights', [])
            if any(topic_lower in t.lower() for t in insight.get('topics', []))
        ]

        if matching_topics or matching_insights:
            results.append({
                'episode': episode,
                'matching_insights': matching_insights
            })

    if not results:
        return f"No results found for topic '{topic}'."

    output = [f"# Results for Topic: '{topic}'\n"]
    output.append(f"Found {len(results)} episode(s)\n")

    for i, result in enumerate(results[:limit], 1):
        ep = result['episode']
        output.append(f"\n## {i}. {ep['guest_name']}: {ep['title']}")
        output.append(f"**Episode:** {ep['id']}")
        output.append(f"**Topics:** {', '.join(ep['topics'])}\n")

        if result['matching_insights']:
            output.append(f"**Insights on '{topic}' ({len(result['matching_insights'])}):**\n")
            for insight in result['matching_insights'][:3]:
                output.append(f"- **{insight['id']}**")
                output.append(f"  > \"{insight['quote'][:100]}...\"")
                output.append(f"  {insight['insight'][:150]}...")
                output.append("")

    return "\n".join(output)


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
