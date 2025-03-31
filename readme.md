
*Project Structure*
fastapi_project/
│── main.py
│── models.py
│── schemas.py
│── database.py
│── crud.py
│── requirements.txt





# Request Model Get
[get](https://api.meteomatics.com/2025-03-31T13:00:00Z/t_2m:C/-22.9068,-43.1729/json)
*model response*
{
  "version": "3.0",
  "user": "ipnetbyvivo_matosferreira_andr",
  "dateGenerated": "2025-03-31T13:14:56Z",
  "status": "OK",
  "data": [
    {
      "parameter": "t_2m:C",
      "coordinates": [
        {
          "lat": -22.9068,
          "lon": -43.1729,
          "dates": [
            {
              "date": "2025-03-31T13:00:00Z",
              "value": 29.1
            }
          ]
        }
      ]
    }
  ]
}



Current task
In the path parameter chant latitude and longitude for city and state name


Eu queria criar por min mesmo, consegue dividir em steps? Por exemplo trabalhar o arquivo x pra depois ir para o y, ir aprendendo os conceitos e boas práticas e ir avançando para o final do projeto, entender a proposta e tudo, gostaria de criar um api que consumisse uma api externa de weather, onde o user api desse alguns put request sobre a localizacao de uma cidade/estado e a api retona-se um json com as informações de weather, seria legal para entender os conceitos básicos, né?
(1) Pesquise sobre os fundamentos de APIs (Application Programming Interfaces) e como elas funcionam para entender a proposta do projeto.
(2) Busque informações sobre diferentes linguagens de programação populares para desenvolvimento de APIs, como Python, Node.js e Go, e compare suas vantagens e desvantagens para iniciantes.
(3) Para a linguagem escolhida, encontre tutoriais e documentação sobre como criar um servidor web básico e lidar com requisições HTTP (especialmente o método PUT).
(4) Pesquise por APIs de clima gratuitas ou com planos gratuitos que permitam buscar informações meteorológicas por cidade ou estado.
(5) Aprenda como fazer requisições HTTP a partir da linguagem de programação escolhida para consumir a API de clima externa.
(6) Descubra como processar a resposta da API de clima, que geralmente estará no formato JSON, e extrair as informações relevantes.
(7) Estude como construir um endpoint de API que aceite requisições PUT com informações de localização (cidade/estado) e retorne os dados climáticos em formato JSON.
(8) Investigue as melhores práticas para o desenvolvimento de APIs, incluindo tratamento de erros, validação de dados de entrada e organização do código.