# Thunderbird+4 #

* Autor : Pierre-Louis Renaud, Daniel Poiraud
* URL : [Documentação](https://www.rptools.org/Outils-DV/NVDA-ThunderbirdPlus-pt.html) , [contato em francês ou inglês](https://www.rptools.org/Outils-DV/contact.html) ;
* Download :
	* [versão estável][1]
	* [Última versão no RPTools.org][2]
* Compatibilidade NVDA :
	* versão mínima : 2019.3 ; 
	* última versão testada: 2023.1 ;
* Compatibilidade com Thunderbird: versões 102.x ;
* [Veja o código-fonte no GitHub][3]

Observação: esta extensão não é compatível com a extensão Mozilla Apps Enhancements. Se você tiver a extensão Mozilla Apps Enhancements instalada, deverá desativá-la ou desinstalá-la antes de usar esta extensão.

Esta extensão melhora muito o conforto e a eficiência da utilização do cliente de correio electrónico Mozilla Thunderbird com o NVDA.

* Abertura melhorada do Thunderbird: 
Quando o Thunderbird é iniciado, o foco pode ser colocado na árvore de pastas ou na lista de mensagens, dependendo da sua escolha no menu de opções. Para outros separadores, o foco é colocado no conteúdo do separador activo;
* Verbosidade Reduzida:
	* Quando o Thunderbird é iniciado, o NVDA já não anuncia informações redundantes;
	* Os alertas "tal pessoa solicitou um recibo de recepção" podem ser desactivados através de uma opção;
	* Os alertas "Isto é um rascunho" e "Thunderbird pensa que esta mensagem é fraudulenta" são simplesmente silenciados;	* Opções para desactivar o anúncio de nomes de listas de correio, remover ou agrupar as menções "RE", e silenciar os endereços de correio electrónico na lista de mensagens;
* Melhoria da navegação. :
	* A passagem para o painel seguinte é feita com a tecla TAB enquanto a tecla Escape é utilizada para regressar ao painel anterior. Isto é mais confortável do que F6 e Shift+F6. 
	* Dois diálogos de contas e suas pastas associadas permitem filtrá-las por palavra-chave ou exibir apenas pastas com mensagens não lidas;
	* Na árvore de pastas, dois atalhos de teclado permitem a navegação entre pastas com mensagens não lidas;
	* Três modos de leitura de texto de mensagem sem deixar a lista de mensagens:
		* Visualização rápida e filtrada do texto da mensagem com espaço, Alt+ seta para baixo ou F4: os cabeçalhos dos blocos grandes nas citações das mensagens são substituídos pela frase "O nome do remetente escreveu". O NVDA anunciará também "link" em vez do endereço longo do link.
		* Visão rápida das citações em ordem cronológica, de baixo para cima, via Shift+Space, Alt+seta acima ou Shift+F4 ;
	* Fácil acesso aos anexos através do atalho Alt+ PageDown ou do número 1 no teclado alfanumérico, pressionado duas vezes; * - Janela para escrever mensagens:
	* Alt+1 anuncia o Remetente, Alt+2 o Destinatário, Alt+3 os anexos, etc. pressionar Duas vezes coloca o foco num destes campos. Alt+m move para  o corpo da mensagem;
	* No diálogo de verificação ortográfica : 
		* a palavra mal escrita é anunciada antes da palavra sugerida. Os atalhos NVDA+Tab ou Alt+seta acima anunciam as palavras mal escritas e substituídas: Pressionadas 1 vez soletram as palavras à velocidade normal, 2 vezes soletram-nas rapidamente, 3 vezes copiam a palavra mal escrita para a área de transferência, para análise num outro campo de edição; 
		* várias combinações da tecla enter activam os botões Substituir, Substituir tudo, Ignorar, Ignorar Tudo ou Adicionar palavra ao Dicionário foram adicionados para maior comodidade neste diálogo; 
	* Barra de filtragem rápida tornada acessível e gestão de etiquetas simplificada. :
	* É possível navegar através das opções de filtro, utilizando as setas verticais. A tecla Enter é utilizada para verificar ou desmarcar uma opção;
	* A adição ou remoção de etiquetas é feita pressionando Shift+um número no teclado alfanumérico. Por exemplo, pressione 4 para adicionar o rótulo "Pendente" a uma mensagem. A lista de mensagens pode então ser filtrada por etiqueta através da barra de filtro rápido que está agora disponível;
- Outras características:
	* A escolha das colunas e a sua disposição na lista de mensagens é tornada acessível através de um simples diálogo;
	* Consulta das colunas da lista de mensagens: permite reproduzir, soletrar ou copiar facilmente o nome do remetente, o assunto ou a data de uma mensagem pressionando um número do teclado alfanumérico, por exemplo anuncia o remetente, pressionando 2 vezes soletra o nome e 3 vezes copia para a área de transferência;
	* Consulta dos cabeçalhos do painel de cabeçalhos apresentado com F8: com Alt+número, uma vez anuncia um cabeçalho, 2 vezes abre um diálogo permitindo copiá-lo, 3 vezes abre o menu contextual nativo Thunderbird associado ao cabeçalho;
* E muitas outras coisas que você descobrirá lendo o [manual do usuário][4] ;


[1]: https://github.com/RPTools-org/ThunderbirdPlus/releases/download/v4.5/ThunderbirdPlus-v4.5-TB102.nvda-addon

[2]: https://www.rptools.org/?p=8610

[3]: https://github.com/RPTools-org/ThunderbirdPlus/

[4]: https://www.rptools.org/Outils-DV/NVDA-ThunderbirdPlus-pt_PT.html