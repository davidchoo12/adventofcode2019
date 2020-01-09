import math

x = '''1 BNZK => 2 NMDF
3 KPQPD => 4 GSRWZ
2 ZRSFC => 7 SRGL
5 XNPDM, 1 FGCV => 7 HMTC
18 LHTNC, 1 WGXGV => 9 CDKF
24 BMQM => 5 FKHRJ
2 LFPNB => 6 XNSVC
9 ZKFRH, 4 XGPLN, 17 SPQP, 2 GVNTZ, 1 JMSCN, 9 SHQN, 1 DZLWC, 18 MSKQ => 7 TXDQK
2 QFTW => 9 JPZT
1 KJCK, 1 TFKZ, 2 XNSVC => 7 GQRB
16 JPZT, 3 DCPW => 7 KJCK
24 LGKPJ, 11 CDKF, 2 HVZQM => 7 RNXJ
1 NMDF, 16 DBLGK, 1 HVZQM => 7 ZKFRH
4 TXDQK, 55 TNZT, 39 KDTG, 6 NVBH, 15 SDVMB, 53 XVKHV, 28 FKHRJ => 1 FUEL
3 CDKV, 11 FGCV => 1 NVBH
3 SPNRW, 7 JMSCN => 9 XMCNV
14 FGCV, 3 CQLRM, 1 TFKZ => 6 PQVBV
5 KJCK, 10 DCPW => 7 DSKH
5 NMDF, 1 TFKZ => 5 DZLWC
1 TNZT => 6 RTSBT
178 ORE => 6 XVLBX
1 SPNRW => 5 CWKH
15 ZRSFC, 2 PQVBV, 2 SRGL => 3 SPNRW
1 SHQN, 7 XNSVC => 4 QWMZQ
5 NVBH, 41 SHQN => 4 BNZK
1 CDKV, 6 KJCK => 4 TNZT
5 ZTBG, 1 HVZQM, 27 CDKV, 1 LHTNC, 2 RTSBT, 2 SHQN, 26 DZLWC => 9 KDTG
11 CDKV => 7 SHQN
13 QWMZQ, 19 FCFG => 7 GVNTZ
1 SHQN, 4 XNSVC => 9 ZRSFC
2 ZKFRH, 9 HVZQM, 1 KJCK, 3 GQRB, 11 DBLGK, 8 DZLWC, 2 SPQP, 5 RNXJ => 8 SDVMB
5 SPNRW => 7 JMSCN
2 XVLBX, 19 KPQPD => 7 XNPDM
2 JPZT => 8 CDKV
1 GQRB => 7 MSKQ
1 SHQN, 13 DSKH => 3 MHQVS
9 JPZT => 8 LFPNB
15 SPNRW, 4 GQRB => 9 SPQP
1 JPZT => 3 TFKZ
1 BMQM => 6 FGCV
24 FKHRJ => 9 DCPW
2 GSRWZ => 8 XGPLN
5 QPSDR, 1 XVLBX => 6 BMQM
128 ORE => 7 QPSDR
2 LHTNC, 6 FCFG, 5 GVNTZ => 7 ZTBG
9 KJCK, 6 MHQVS, 5 NVBH => 6 KRDGK
3 HMTC, 4 QWMZQ => 2 FCFG
4 WGXGV, 5 PQVBV => 1 LGKPJ
42 XVLBX => 5 CQLRM
1 CWKH => 9 DBLGK
1 KRDGK, 2 GQRB, 12 TFKZ => 5 LHTNC
1 CQLRM, 1 HMTC => 8 WGXGV
116 ORE => 1 QFTW
13 XMCNV => 5 XVKHV
12 LGKPJ, 8 FKHRJ => 9 HVZQM
5 QPSDR => 6 KPQPD'''

lines = x.split('\n')
dependencies = {} # {'NMDF': {'count': 2, 'inputs': [{'count': 1, 'chem': 'BNZK'}, ...]}, ...}
for line in lines:
  io = line.split(' => ')
  inputs = io[0].split(', ')
  inputs = [{ 'count': int(inp.split(' ')[0]), 'chem': inp.split(' ')[1] } for inp in inputs]
  output = io[1]
  [output_count, output_chem] = output.split(' ')
  dependencies[output_chem] = { 'count': int(output_count), 'inputs': inputs }
fuel_deps = { inp['chem']: inp['count'] for inp in dependencies['FUEL']['inputs'] } # {'A': 7, ...}
# print(dependencies)
# while len(fuel_deps) > 1 or 'ORE' not in fuel_deps.keys():
while not all(k == 'ORE' or v <= 0 for k, v in fuel_deps.items()):
  print(fuel_deps)
  new_fuel_deps = {}
  for fd_chem, fd_amount in fuel_deps.items():
    if fd_chem == 'ORE' or fd_amount < 0:
      continue
    reaction = dependencies[fd_chem]
    amount_per_reaction = reaction['count']
    reaction_count = fd_amount / amount_per_reaction
    reaction_count = math.ceil(reaction_count)
    print(f'fd_chem {fd_chem}, fd_amount {fd_amount}, reaction_count {reaction_count}')
    print(str(reaction['count']) + ' ' + fd_chem + ' <= ' + ', '.join([f'{i["count"]} {i["chem"]}' for i in reaction['inputs']]))
    new_fuel_deps.setdefault(fd_chem, fuel_deps.get(fd_chem) or 0)
    new_fuel_deps[fd_chem] -= amount_per_reaction * reaction_count
    for inp in reaction['inputs']:
      new_fuel_deps.setdefault(inp['chem'], fuel_deps.get(inp['chem']) or 0)
      new_fuel_deps[inp['chem']] += inp['count'] * reaction_count
      print(f'new_fuel_deps[{inp["chem"]}] {new_fuel_deps[inp["chem"]]}, new_fuel_deps[{fd_chem}] {new_fuel_deps[fd_chem]}')
  fuel_deps = new_fuel_deps
print(fuel_deps)
print(fuel_deps['ORE'])