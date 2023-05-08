from langchain.document_loaders.csv_loader import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os

OpenAI.api_key = os.getenv('OPENAI_API_KEY')

#load the CSV file
loader = CSVLoader(file_path='file.csv')

#create index
index_creator = VectorstoreIndexCreator()
docsearch = index_creator.from_loaders([loader])

#create QA chain
chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff",
                                    retriever=docsearch.vectorstore.as_retriever(), input_key="question")

#pass questions to the chain
query = "<Replace with your question>?"
response = chain({"question": query})

print(response)