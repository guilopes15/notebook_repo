## Proxy
Intercepta/filtra as requisições da intranet

``` mermaid 
graph LR
  A[Pcs da rede] --> E{Roteador};
  B[Pcs da rede] --> E;
  C[Pcs da rede] --> E;
  D[Pcs da rede] --> E;
  E --> F[Servidor Proxy];
  F --> G{Internet};

```
<br>
<br>
<br>

## Reverse Proxy
Protege/Balanceia as requisições da internet
``` mermaid 
graph LR
  A[User PC] --> D{Internet};
  B[User PC] --> D;
  C[User PC] --> D;
  D --> E[Reverse Proxy];
  E --> F{Server};
  E --> G{Server};

```
