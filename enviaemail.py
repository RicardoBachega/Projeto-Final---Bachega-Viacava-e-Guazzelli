import smtplib

#     definir email do usuario como: toaddrs  = "exemplo@exemplo.exemplo"

def envia_email(texto, toaddrs):
    fromaddr = "ricardonb@al.insper.edu.br"
    # Add the From: and To: headers at the start!
    msg = (texto.format(fromaddr, toaddrs))
    
    server = smtplib.SMTP('insper.edu.br')
    server.set_debuglevel(1)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    
    aviso = "Enviado para", toaddrs
    
    return aviso

envia_email("Olá, cara!", "ricardo.n.b@hotmail.com")

print(envia_email("Olá, cara!", "ricardo.n.b@hotmail.com"))