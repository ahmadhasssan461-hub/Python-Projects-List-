from groq import Groq
client = Groq(api_key="use your own ")
score = 0
for i in range(5):
  response = client.chat.completions.create(
    model = "llama-3.1-8b-instant",
    messages=[{
      "role" : "user", 
      "content": f"Ask me exactly ONE simple general knowledge question. Question number {i+1}, make it different from previous questions. Just the question only, nothing else."
    }]    
  )
  question = response.choices[0].message.content
  print(question)
  answer = input("Enter Your Answer : ")
  check = client.chat.completions.create(
    model = "llama-3.1-8b-instant",
    messages=[{
      "role" : "user", 
      "content": f"Question: {question} Answer: {answer} Reply with only one word: 'Correct' or 'Incorrect'" 
    }]    
  )
  result = check.choices[0].message.content

  print(result)

  if result.strip().lower() == "correct":
    score += 1
print(f"\nFinal Score: {score}/5")