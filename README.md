# LDS1-sistema-matricula

Sistema de Matrículas para uma Universidade

# Alunos

### Caio Costa

![Caio](/img/profileCaio.png)

<hr />

### Gustavo Oliveira

![Gustavo](/img/profileGustavo.png)

<hr />

### Luis Brescia

![Luis](/img/profileLuis.png)

<hr />

### Victor Reis Carlota

![Victor](/img/profileVictor.png)

# Diagrama de Caso de Uso

![Diagrama de Caso de Uso](/img/UseCaseMatriculaa.png)

# Histórias de Usuário

### Como aluno quero

- Visualizar o histórico de disciplinas cursadas e notas recebidas.
- Visualizar os horários das disciplinas
- Me matricular em até 4 disciplinas obrigatórias e 2 optativas.
- Cancelar matrículas realizadas durante o período de matrículas.
- Poder acessar o sistema e realizar o login para verificar minhas disciplinas matriculadas.
- Ser notificado se uma disciplina que me matriculei for cancelada devido ao número insuficiente de alunos.

### Como professor quero

- Visualizar a lista de alunos matriculados em cada disciplina que ministro.
- Atualizar as notas dos alunos em cada disciplina que ministro.
- Acessar o sistema e realizar o login para verificar minhas turmas.

### Como secretaria quero

- Gerar o currículo semestral com as disciplinas disponíveis para os cursos.
- Gerenciar as disciplinas, cadastrando novas ou desativando disciplinas antigas.
- Gerenciar os professores, associando-os às disciplinas que ministrarão.
- Gerenciar os alunos, mantendo um cadastro atualizado.
- Garantir que as disciplinas com menos de 3 alunos sejam automaticamente canceladas no final do período de matrículas.
- Notificar o sistema de cobranças após a matrícula do aluno, para que seja gerada a cobrança correspondente.

### Como sistema de cobranças

- Ser notificado pelo sistema de matrículas após o aluno se inscrever em disciplinas, para gerar a cobrança do semestre.
- Ser capaz de ajustar cobranças caso um aluno cancele uma disciplina dentro do período permitido.

# Diagrama de Classes

![Diagrama de Classes](/img/ClassDiagram.png)