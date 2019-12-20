#encoding='utf-8'
import json
name_emb = {"a":1111, "b":22222,"c": 232323}
jsDumps = json.dumps(name_emb)
print(type(jsDumps), "Json dumps:",jsDumps)
jsLoads = json.loads(jsDumps)
print(type(jsLoads),"json loads:", jsLoads)
 