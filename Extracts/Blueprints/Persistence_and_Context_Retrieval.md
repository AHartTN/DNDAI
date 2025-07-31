# Persistence and Context Retrieval for AI Dungeon Master

## Data Architecture
- Categorize campaign data, history, lore, and user-generated content.
- Implement deduplication and versioning for unique content.

## T-SQL Schema
- Define normalized tables: Campaigns, Sessions, Characters, Locations, Items, LoreEntries, Events, CharacterStates, Relationships, VectorEmbeddings.

## Context Retrieval
- Use stored procedures, views, and targeted queries for efficient context extraction.
- Apply RAG (Retrieval Augmented Generation) patterns for AI context.

## Semantic Search
- Store vector embeddings in T-SQL/VARBINARY(MAX).
- Recommend hybrid vector DB for scalable semantic search.
