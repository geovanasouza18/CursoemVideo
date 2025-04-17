let NivelAcesso = Number(prompt("Informe seu nível de acesso"))

if(NivelAcesso >=5 && NivelAcesso <=10){
    alert("Acesso autorizado. Bem-vindo ao sistema confidencial.")
}else if(NivelAcesso >=1 && NivelAcesso <=4){
    alert("Acesso negado. Nível insuficiente para entrar no sistema.")
}else{
    alert("Alerta! Possível invasor detectado.")
}
