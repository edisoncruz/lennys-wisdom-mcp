# Lenny's Wisdom MCP Server - Phase 1 Complete! 🎉

**Date:** January 30, 2026
**Status:** Foundation Complete, Ready for Extraction (when budget allows)

---

## 📋 Quick Summary

We've completed **Phase 1** of building an MCP server that will give Claude users instant access to wisdom from all 298 Lenny's Podcast episodes. Here's what's ready:

✅ **Complete JSON schema design** (6 entity types)
✅ **Validation tooling** (working Python script)
✅ **Sample data** (all entities, validated)
✅ **Extraction pipeline architecture** (7-stage process)
✅ **Access to all 298 transcripts** (verified and analyzed)
✅ **Cost estimates** (~$150-$300 for API extraction)

**Next step:** When ready to proceed, we'll build extraction scripts and process episodes (requires Anthropic API account).

---

## 🎯 What We're Building

**Vision:** "Plug into the collective wisdom of 300+ world-class product leaders"

An MCP server that provides:
- **search_wisdom(query)** → Synthesized answers with multi-guest citations
- **get_framework(name)** → Structured frameworks like "Radical Candor"
- **ask_expert(guest, question)** → Channel specific guests' philosophy
- **get_perspectives(topic)** → Multiple viewpoints on topics
- **solve_situation(situation)** → Step-by-step playbooks

**Why it matters:** Meet users in their workflow (Claude/ChatGPT) with curated wisdom, not just raw transcript search.

---

## 📊 Data Foundation Designed

### Six Entity Types (Schemas Complete)

| Entity | Count Target | Description |
|--------|-------------|-------------|
| **Episodes** | 298 | Full episodes with metadata, themes, insights |
| **Quotes** | ~3,500 | Memorable quotes (12 per episode avg) |
| **Frameworks** | 50-100 | Named frameworks like Radical Candor, Founder Mode |
| **Situations** | 30-50 | Playbooks for specific scenarios (e.g., "firing a friend") |
| **Guests** | 298+ | Guest profiles with expertise and philosophy |
| **Topics** | 50-100 | Taxonomy for categorization |

### Sample Data Created

All examples validate against schemas:
- **Brian Chesky episode** - Founder mode, product management, culture
- **Radical Candor framework** - Kim Scott's 2x2 feedback matrix
- **Matt Mochary quote** - "If you haven't fired someone you regretted..."
- **"Firing a friend" situation** - 5-step playbook with expert perspectives
- **Brian Chesky guest profile** - Philosophy and signature frameworks
- **Leadership topic** - Hierarchical topic taxonomy

---

## 💰 Cost Estimates (When Ready to Extract)

### Full Extraction via Anthropic API

**Using Claude Sonnet 4.5:** ~$306 total
- Episode metadata: $89
- Insight extraction: $90
- Framework detection: $75
- Cross-referencing: $15
- Situation synthesis: $37

**Using Claude Haiku (cheaper):** ~$150 total
- Use Haiku for simpler tasks (metadata, basic extraction)
- Use Sonnet only for complex tasks (frameworks, synthesis)
- 50% cost savings

### What This Requires

1. **Anthropic API account** (separate from Claude.ai subscription)
   - Sign up at console.anthropic.com
   - Add payment method
   - Get API key

2. **One-time cost** for processing all 298 episodes
   - Not covered by Claude.ai Max plan
   - Separate billing

### Budget-Friendly Options

**Option 1: Phased extraction**
- Start with 20-30 most valuable episodes (~$20-30)
- Validate quality
- Decide whether to continue

**Option 2: Manual extraction via Cowork**
- Use Claude in Cowork mode to manually extract episodes
- No API costs (covered by Max plan)
- Very time-consuming (weeks of manual work)

**Option 3: Hybrid approach**
- API for bulk processing
- Manual for quality control and refinement

---

## 📁 Transcripts Ready

**Found in your folder:** 298 transcript files

**Format:**
```
Brian Chesky (00:00:00):
Way too many founders apologize for how they want to run the company...

Lenny (00:01:01):
Today my guest is Brian Chesky...
```

**Quality:** High - clean, well-formatted with timestamps
**Average size:** ~14-16K words per transcript
**Perfect for extraction!**

### Sample Guests
- Brian Chesky (Airbnb)
- Kim Scott (Radical Candor)
- Adam Grant
- Matt Mochary
- Patty McCord
- Claire Hughes Johnson
- And 292 more...

---

## 🔧 Extraction Pipeline (Designed & Ready)

### 7-Stage Process

```
1. Preparation        → Organize transcripts
2. Episode Metadata   → Extract summaries, topics, themes (LLM)
3. Insight Extraction → Find 8-15 key quotes per episode (LLM)
4. Framework Detection → Identify & extract frameworks (LLM)
5. Cross-Referencing  → Link all entities (programmatic + LLM)
6. Situation Synthesis → Create playbooks from multiple episodes (LLM)
7. Validation & QA    → Schema validation + quality checks
```

### Technology Stack

**Core:**
- Python 3.10+
- Claude API (Anthropic SDK)
- Pydantic for data validation
- JSON files (can migrate to SQLite later)

**Tools:**
- JSON Schema validators
- Validation CLI script
- Extraction scripts (to be built)
- MCP server (FastMCP)

---

## 🚀 Next Steps (When You Resume)

### Immediate Next Session

1. **Set up Anthropic API account**
   - console.anthropic.com
   - Add payment method
   - Get API key
   - Budget $150-300

2. **Build extraction scripts**
   - Episode metadata extractor
   - Insight/quote extractor
   - Framework detector
   - Test on 2-3 sample episodes

3. **Validate pipeline**
   - Run on Brian Chesky, Kim Scott, Matt Mochary
   - Check quality
   - Refine prompts
   - Measure actual costs

### Following Sessions

4. **Bulk extraction** (5-8 sessions)
   - Process all 298 episodes
   - Extract ~3,500 quotes
   - Detect ~80 frameworks
   - Build cross-reference indices

5. **Situation synthesis** (3-5 sessions)
   - Create 30-50 playbooks
   - Synthesize from multiple episodes
   - Human review high-value content

6. **MCP Server** (3-5 sessions)
   - Implement 5 core tools
   - Test with Claude Desktop
   - Deploy to hosting

7. **Launch!** (2-3 sessions)
   - Landing page
   - Documentation
   - Ship to community

---

## 📝 What's Been Documented

### Key Documents Created (in this folder)

1. **This README** - Project overview and status
2. **Schema Design** - Complete data structure documentation
3. **Extraction Pipeline** - Technical architecture
4. **Validation Script** - Data quality checks

### Schemas Created

All in `schemas/` folder:
- `episode.schema.json` - Episode structure
- `framework.schema.json` - Framework structure
- `quote.schema.json` - Quote structure
- `situation.schema.json` - Situation playbook structure
- `guest.schema.json` - Guest profile structure
- `topic.schema.json` - Topic taxonomy structure

### Sample Data

All in `sample_data/` folder with subdirectories:
- `episodes/` - Brian Chesky example
- `frameworks/` - Radical Candor example
- `quotes/` - Matt Mochary example
- `situations/` - "Firing a friend" playbook
- `guests/` - Brian Chesky profile
- `topics/` - Leadership taxonomy

---

## 🎯 Success Criteria

### Phase 1 ✅ COMPLETE
- [x] JSON schemas finalized
- [x] Validation tooling working
- [x] Sample data created and validated
- [x] Extraction pipeline designed
- [x] Access to all transcripts

### Phase 2 (Next: Extraction)
- [ ] Anthropic API account set up
- [ ] Extraction scripts built
- [ ] All 298 episodes extracted
- [ ] 50+ frameworks documented
- [ ] 30+ situation playbooks created
- [ ] Quality validation passed

### Phase 3 (MCP Server)
- [ ] 5 core MCP tools implemented
- [ ] Deployed and accessible
- [ ] Claude Desktop integration working

### Phase 4 (Launch)
- [ ] Landing page live
- [ ] Documentation complete
- [ ] Community feedback
- [ ] GitHub repository public

---

## 💡 Key Design Decisions

### Why JSON Files (Not SQLite)?
- Easier to inspect and debug
- Version control friendly (can track in git)
- Simple extraction pipeline
- Can migrate to SQLite in Phase 2

### Why Two-Pass Framework Extraction?
- Pass 1: Detect presence (cheap)
- Pass 2: Full extraction (expensive)
- Saves ~50% on framework extraction costs

### Why Situation Synthesis Last?
- Requires multiple episodes as input
- Uses long-context Claude
- High-value content worth manual review
- Can leverage all extracted data

---

## 📞 When You Resume

**To pick up where we left off:**

1. Open Cowork mode
2. Reference this README
3. Say: "Let's continue with Lenny's Wisdom MCP. I'm ready to set up the API and start extraction."

**What to have ready:**
- Anthropic API key (from console.anthropic.com)
- Budget allocation ($150-300)
- Time for 3-5 sessions to build extraction scripts

**What I'll do:**
- Build extraction scripts
- Test on sample episodes
- Process all 298 episodes
- Generate complete dataset
- Build MCP server

---

## 🎉 What We Accomplished (Phase 1)

In this session, we:

1. ✅ Designed comprehensive JSON schemas (6 entity types)
2. ✅ Created JSON Schema validators
3. ✅ Built validation CLI tool with beautiful output
4. ✅ Generated realistic sample data for all entities
5. ✅ Validated all samples successfully (6/6 pass)
6. ✅ Documented complete extraction pipeline
7. ✅ Estimated costs and timeline
8. ✅ Accessed and analyzed all 298 transcripts
9. ✅ Created comprehensive project documentation

**Phase 1 foundation is solid!** We're ready to extract when you're ready to invest in the API.

---

## 🤔 Questions to Consider

Before resuming:

1. **Budget:** Comfortable with $150-300 one-time API cost?
2. **Timing:** Want full extraction (298 episodes) or start small (20-30)?
3. **Approach:** Bulk API extraction or manual via Cowork?
4. **Hosting:** GitHub public repo or keep private?
5. **Licensing:** MIT license for the data and code?

---

## 📚 Additional Resources

- **MCP Documentation:** modelcontextprotocol.io
- **Anthropic API Docs:** docs.anthropic.com
- **FastMCP Library:** github.com/jlowin/fastmcp
- **Lenny's Podcast:** lennyspodcast.com

---

**Project Status:** Phase 1 Complete ✅
**Next Phase:** Extraction (paused until February, API setup)
**Timeline:** 2-4 weeks from API setup to launch
**Total Budget:** $150-300 (API) + $0-7/month (hosting)

Looking forward to building this with you in February! 🚀

---

*Created: January 30, 2026*
*By: Claude (Cowork Mode)*
*For: Edison Cruz (edisoncruz@gmail.com)*
