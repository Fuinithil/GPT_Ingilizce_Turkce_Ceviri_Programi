import openai

openai.api_key = "api_key" #Bu kısma openai üzerinden aldığınız api key'i girmeniz gerekiyor

while True:

    text = input("Çevirmek istediğiniz kelimeyi giriniz: ")

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Translate to Turkish: {text}",
        temperature=0
        )

    print(response["choices"][0]["text"])