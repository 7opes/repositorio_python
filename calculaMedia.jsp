<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <title>Resultado da Média</title>
</head>
<body>
    <h2>Resultado da Média</h2>
    <% 
        try {
            // Recebe as notas do formulário
            double nota1 = Double.parseDouble(request.getParameter("nota1"));
            double nota2 = Double.parseDouble(request.getParameter("nota2"));
            
            // Calcula a média
            double media = (nota1 + nota2) / 2.0;
    %>
            <p>Nota 1: <%= nota1 %></p>
            <p>Nota 2: <%= nota2 %></p>
            <p>Média: <%= media %></p>
    <%
        } catch (NumberFormatException e) {
            out.println("<p style='color:red;'>Erro: Insira valores numéricos válidos para as notas.</p>");
        }
    %>
</body>
</html>
