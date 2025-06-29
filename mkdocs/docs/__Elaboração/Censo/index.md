<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Censo - Ilha Primeira</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Censo - Ilha Primeira</h1>
  <form id="censoForm">
    <!-- 1. IDENTIFICAÇÃO DO DOMICÍLIO -->
    <fieldset>
      <legend>1. Identificação do Domicílio</legend>
      <label>UF: <input name="uf" required></label>
      <label>Município: <input name="municipio" required></label>
      <label>Distrito: <input name="distrito"></label>
      <label>Tipo de Domicílio:
        <select name="tipoDomicilio" required>
          <option value="1">Particular Permanente</option>
          <option value="5">Particular Improvisado</option>
          <option value="6">Coletivo com Morador</option>
        </select>
      </label>
      <label>Tipo de Construção:
        <select name="tipoConstrucao">
          <option value="011">Casa</option>
          <option value="012">Casa de Vila</option>
          <option value="013">Apartamento</option>
          <option value="014">Cortiço</option>
          <option value="015">Habitação Indígena</option>
        </select>
      </label>
    </fieldset>
    <!-- 2. MORADORES -->
    <fieldset>
      <legend>2. Moradores</legend>
      <label>Nome: <input name="moradorNome" required></label>
      <label>Sobrenome: <input name="moradorSobrenome" required></label>
      <label>Sexo:
        <select name="moradorSexo">
          <option value="1">Masculino</option>
          <option value="2">Feminino</option>
        </select>
      </label>
      <label>Data de Nascimento: <input type="date" name="moradorNascimento"></label>
      <label>Parentesco com o responsável:
        <select name="parentesco">
          <option value="01">Responsável</option>
          <option value="02">Cônjuge Sexo Diferente</option>
          <option value="03">Cônjuge Mesmo Sexo</option>
          <option value="04">Filho(a) do casal</option>
          <option value="05">Filho(a) só do responsável</option>
          <option value="06">Enteado(a)</option>
        </select>
      </label>
    </fieldset>
    <!-- 3. CARACTERÍSTICAS DO DOMICÍLIO -->
    <fieldset>
      <legend>3. Características do Domicílio</legend>
      <label>Forma de Abastecimento de Água:
        <select name="aguaForma">
          <option value="1">Rede Geral</option>
          <option value="2">Poço Artesiano</option>
          <option value="3">Poço Raso</option>
          <option value="4">Fonte/Mina</option>
        </select>
      </label>
      <label>Banheiros Exclusivos: <input type="number" name="banheiros"></label>
      <label>Destino do Lixo:
        <select name="destinoLixo">
          <option value="1">Coletado</option>
          <option value="2">Caçamba</option>
          <option value="3">Queimado</option>
          <option value="4">Enterrado</option>
          <option value="5">Jogado em terreno</option>
          <option value="6">Outro</option>
        </select>
      </label>
    </fieldset>
    <!-- 4. IDENTIFICAÇÃO ÉTNICO-RACIAL -->
    <fieldset>
      <legend>4. Etnia/Raça</legend>
      <label>Cor/Raça:
        <select name="corRaca">
          <option value="1">Branca</option>
          <option value="2">Preta</option>
          <option value="3">Amarela</option>
          <option value="4">Parda</option>
          <option value="5">Indígena</option>
        </select>
      </label>
      <label>Você se considera indígena?
        <select name="indigena">
          <option value="1">Sim</option>
          <option value="2">Não</option>
        </select>
      </label>
      <label>Fala Língua Indígena?
        <select name="falaLinguaIndigena">
          <option value="1">Sim</option>
          <option value="2">Não</option>
        </select>
      </label>
    </fieldset>
    <!-- 5. REGISTRO CIVIL -->
    <fieldset>
      <legend>5. Registro Civil</legend>
      <label>Tipo de Registro:
        <select name="registro">
          <option value="1">Cartório</option>
          <option value="2">RANI</option>
          <option value="3">Não tem</option>
          <option value="4">Não sabe</option>
        </select>
      </label>
    </fieldset>
    <!-- 6. EDUCAÇÃO -->
    <fieldset>
      <legend>6. Educação</legend>
      <label>Sabe ler e escrever?
        <select name="alfabetizado">
          <option value="1">Sim</option>
          <option value="2">Não</option>
        </select>
      </label>
    </fieldset>
    <!-- 7. TRABALHO E RENDIMENTO -->
    <fieldset>
      <legend>7. Trabalho e Renda</legend>
      <label>Tipo de rendimento:
        <select name="tipoRenda">
          <option value="1">Em dinheiro</option>
          <option value="2">Outra forma</option>
          <option value="3">Não tem</option>
        </select>
      </label>
      <label>Faixa de Renda:
        <select name="faixaRenda">
          <option value="1">1 a 500</option>
          <option value="2">501 a 1000</option>
          <option value="3">1001 a 2000</option>
          <option value="4">2001 a 3000</option>
          <option value="5">3001 a 5000</option>
          <option value="6">5001 a 10000</option>
        </select>
      </label>
    </fieldset>
    <!-- 8. MORTALIDADE -->
    <fieldset>
      <legend>8. Mortalidade</legend>
      <label>Houve falecimento desde 2019?
        <select name="houveObito">
          <option value="1">Sim</option>
          <option value="2">Não</option>
        </select>
      </label>
      <label>Nome do falecido: <input name="nomeFalecido"></label>
      <label>Idade ao falecer: <input type="number" name="idadeFalecido"></label>
    </fieldset>
    <!-- 9. PRESTAÇÃO DAS INFORMAÇÕES -->
    <fieldset>
      <legend>9. Quem Preencheu?</legend>
      <label>
        <select name="quemPreencheu">
          <option value="1">A própria pessoa</option>
          <option value="2">Outro morador</option>
          <option value="3">Não morador</option>
        </select>
      </label>
      <label>Nome do informante (se outro morador): <input name="nomeInformante"></label>
    </fieldset>
    <button type="submit">Enviar</button>
    <button type="button" onclick="exportToJSON()">Exportar para JSON</button>
    <button type="button" onclick="exportToCSV()">Exportar para CSV</button>

  </form>
  <script src="script.js"></script>
</body>
</html>