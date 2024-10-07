# Vamos rodar o servidor agora

from src.main.server.server import app

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
# o host vai ser a minha própria máquina
# Em ambientes de produção usamos o debug como false
