from bm25 import BM25

documents = [
    "This report discusses the design of the Mars Rover and its scientific mission objectives.",
    "A study on the aerodynamics of space vehicles in the re-entry phase into Earth's atmosphere.",
    "Analysis of satellite communication protocols for deep space exploration missions.",
    "Investigation into solar panel efficiency improvements for long-duration space flights.",
    "Research on autonomous navigation systems for unmanned spacecraft.",
    "Assessment of thermal protection systems used during spacecraft atmospheric re-entry.",
    "Development of AI algorithms to optimize spacecraft trajectory and fuel consumption.",
    "Evaluation of the impact of microgravity on human physiology during extended space missions.",
    "Design and testing of propulsion systems for next-generation launch vehicles.",
    "Study of cosmic radiation effects on spacecraft electronics and countermeasures.",
]

bm25 = BM25(documents)

query = "solar panel efficiency"
results = bm25.search(query)

print(f"Search results for query: '{query}'\n")
for idx, score in results:
    print(f"Doc: {documents[idx]} | Score: {score:.4f}")
