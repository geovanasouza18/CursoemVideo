let idade = Number(prompt("Digite sua idade"))

if(idade <18){
    alert("Menor de idade detectado. Acesso negado e responsáveis serão notificados.")
}else if(idade >=18 && idade <=59){
    alert("Adulto identificado. Analisando nível de acesso...")
}else{
    alert("Agente sênior identificado. Priorizar registro e acompanhamento.")
}