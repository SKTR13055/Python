{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyPovQUhqbDsX/5qInfXkA+H"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":2,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"Lde0QT43hBKX","executionInfo":{"status":"ok","timestamp":1674040052883,"user_tz":-330,"elapsed":11,"user":{"displayName":"Syed KhalidTipu","userId":"03379379984070065292"}},"outputId":"6c43ccfb-d4b3-4b56-d23a-cddd487df5cd"},"outputs":[{"output_type":"stream","name":"stdout","text":["5\n","3\n","2\n","4\n","8\n","7\n"]}],"source":["graph= {\n","    '5':['3','7'],\n","    '3':['2','4'],\n","    '2':[],\n","    '4':['8'],\n","    '7':['8'],\n","    '8':[]\n","}\n","\n","visited = set()\n","\n","def dfs(vistied,graph,node):\n","  if node not in visited:\n","    print(node)\n","    visited.add(node)\n","    for neighbour in graph[node]:\n","      dfs(visited,graph,neighbour) \n","\n","dfs(visited,graph,'5')\n"]}]}