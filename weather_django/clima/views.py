from django.shortcuts import render

def pesquisar_previsao(request):
    return render(request, 'clima/pesquisa.html')  # Renderiza um template HTML de pesquisa

def resultado_previsao(request):
    # Aqui você vai implementar a lógica para exibir o resultado da previsão
    localidade = request.GET.get('localidade')  # Pega a cidade do formulário
    # Implemente a lógica de busca da API e retorno dos dados aqui
    return render(request, 'clima/resultado.html', {'localidade': localidade})