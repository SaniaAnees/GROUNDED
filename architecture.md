ingest: reads files from a folder, splits into text chunks
embed: turns chunks into vectors using a pretrained model
retrieve: finds most relevant chunks via manual cosine similarity
generate: sends question + relevant chunks to AI model, returns claims with sources
verify: checks each claim against its source with local NLI, labels entailment/contradiction/neutral