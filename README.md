# Terminal Menu Generator

This project is a simple menu-based command line tool that allows users to perform different actions by selecting options from a menu. The tool is designed to be extensible and customizable by allowing users to define their own menu options and actions.

## Installation
Clone the project repository to your local machine.
Navigate to the project directory.

## Usage
To run the menu tool, navigate to the project directory and run the command python main.py. This will display the menu options to the user, allowing them to select an option by using the up and down arrow keys and pressing ENTER.

Each menu option is associated with a function that performs a specific action. These functions can be customized by the user to perform any desired action. By default, the tool comes with three sample functions that perform some basic tasks.

The results of the functions can be optionally logged to a file by configuring the logging system. By default, the tool logs DEBUG level messages to a file named log_file.log in the project directory.

<p align="center"><img src="https://user-images.githubusercontent.com/11949740/230423234-284e778e-dadb-4502-8fb9-84bee87ba7f9.png"></p>

## Customization
The tool can be customized by defining new menu options and functions. To define a new menu option, add a new key-value pair to the menu_options dictionary in the main.py file, where the key is the option name and the value is the function that should be executed when the option is selected.

To define a new function, add a new function definition to the main.py file, and then add the function to the menu_options dictionary with a unique key.

To customize the logging system, modify the logging configuration in the main.py file. This can be done by adjusting the log level, changing the log file name, or modifying the log message format.

## Contributions
Contributions to this project are welcome and encouraged. To contribute to the project, follow these steps:

* Fork the project repository to your own account.
* Clone the forked repository to your local machine.
* Create a new branch for your changes.
* Make your changes and commit them to your branch.
* Push your changes to your forked repository.
* Create a pull request to merge your changes into the main project repository.

When making contributions, please ensure that your changes are well-documented and tested, and adhere to the project's coding style and guidelines.

## 🇧🇷
Este projeto é uma ferramenta de linha de comando baseada em menu simples que permite aos usuários executar diferentes ações selecionando opções de um menu. A ferramenta foi projetada para ser extensível e personalizável, permitindo que os usuários definam suas próprias opções e ações de menu.

## Instalação
Clone o repositório do projeto em sua máquina local.
Navegue até o diretório do projeto.

## Uso
Para executar a ferramenta de menu, navegue até o diretório do projeto e execute o comando python main.py. Isso exibirá as opções do menu para o usuário, permitindo que ele selecione uma opção usando as teclas de seta para cima e para baixo e pressionando ENTER.

Cada opção de menu está associada a uma função que executa uma ação específica. Essas funções podem ser personalizadas pelo usuário para executar qualquer ação desejada. Por padrão, a ferramenta vem com três funções de amostra que executam algumas tarefas básicas.

Os resultados das funções podem ser opcionalmente registrados em um arquivo configurando o sistema de registro. Por padrão, a ferramenta registra mensagens de nível DEBUG em um arquivo denominado log_file.log no diretório do projeto.

## Costumização
A ferramenta pode ser personalizada definindo novas opções de menu e funções. Para definir uma nova opção de menu, adicione um novo par chave-valor ao dicionário menu_options no arquivo main.py, onde a chave é o nome da opção e o valor é a função que deve ser executada quando a opção for selecionada.

Para definir uma nova função, adicione uma nova definição de função ao arquivo main.py e, em seguida, adicione a função ao dicionário menu_options com uma chave exclusiva.

Para customizar o sistema de criação de log, modifique a configuração de criação de log no arquivo main.py. Isso pode ser feito ajustando o nível de log, alterando o nome do arquivo de log ou modificando o formato da mensagem de log.

## Contribuições
Contribuições para este projeto são bem-vindas e incentivadas. Para contribuir com o projeto, siga os seguintes passos:

* Fork o repositório do projeto para sua própria conta.
* Clone o repositório bifurcado para sua máquina local.
* Crie uma nova ramificação para suas alterações.
* Faça suas alterações e confirme-as em sua ramificação.
* Envie suas alterações para o repositório bifurcado.
* Crie uma pull resquest  para mesclar suas alterações no repositório principal do projeto.

Ao fazer contribuições, certifique-se de que suas alterações sejam bem documentadas e testadas e siga o estilo de codificação e as diretrizes do projeto.
