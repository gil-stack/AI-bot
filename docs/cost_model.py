"""Budget scenario supplied in continuation, reviewed 2026-11-11. No provider calls."""
from decimal import Decimal, ROUND_HALF_UP
D=lambda x:Decimal(str(x))
FX=D(20); FIX=D('18.6678'); VAT=D('.16'); COUNTS=(25,100,1000)
AI_PER_USER=D(3)*D('.14')+D('.24')*D('.67')
VM_PER_USER=D(24)*D('1.30')
CENTRAL=[
('API / gestor de VMs',[48,48,144],'P×E','C01'),
('Workers centrales',[12,48,144],'P×E','C01'),
('Staging',[12,24,24],'P×E','C01'),
('Backups centrales',[21.6,36,93.6],'P×E','C02'),
('PostgreSQL + disco adicional',[36.9,283,306],'P×E','C03'),
('Valkey / cola y caché',[15,30,60],'P×E','C04'),
('Balanceador',[12,12,24],'P×E','C05'),
('Spaces / archivos compartidos',[5,5,10],'P×E','C06'),
('Cloudflare',[25,25,250],'P×E','C07'),
('Sentry',[29,29,89],'P×E','C08'),
('Resend',[20,20,20],'P×E','C09'),
('GitHub Team',[20,20,40],'P×E','C10'),
('Workspace del equipo',[42,42,84],'P×E','C11'),
('Dominio / renovación prorrateada',[D('19.98')/12]*3,'P×E','C12'),
('Provisión CI/CD adicional',[10,20,60],'R','-'),
('Provisión exceso de logs',[15,30,100],'R','-'),
('Provisión red / tráfico cruzado',[25,50,150],'R','-')]
BUILD_TEAM=[('Líder técnico / backend',1,100000,4),('Ingeniería de IA',1,90000,4),('Backend de pagos',1,85000,4),('Frontend',1,65000,4),('DevOps',D('.5'),80000,4),('QA',D('.5'),45000,4),('UX / diseño',D('.5'),50000,2)]
ONE_OFF=[('Constitución / notario / trámites',30000),('Contratos comerciales y financieros',60000),('Privacidad y acuerdos de tratamiento',30000),('Configuración fiscal / contable',15000),('Pentest y revisión de pagos',90000),('Provisión evaluación OAuth restringido',60000),('Marca / identidad inicial',15000),('4 equipos × MXN 25,000',100000)]
OPS=[('Mantenimiento de software',[40000,80000,160000]),('DevOps / guardias',[20000,20000,40000]),('Atención y conciliación',[7500,15000,60000]),('Contabilidad mensual',[3500,5000,12000]),('Asesoría legal / cumplimiento',[10000,15000,30000])]

def money(x,decimals=2): return f"{D(x).quantize(D(1).scaleb(-decimals),rounding=ROUND_HALF_UP):,.{decimals}f}"

def scenario(i,fx=FX,tasks=20):
 n=D(COUNTS[i]); new=D((25,30,150)[i]); central=sum(D(r[1][i]) for r in CENTRAL)
 secrets=(20+3*n)*(D('.4')+D(30)*D('.05')/10000)
 kyc=max(D(99),new*D('1.39'))+new*D('.64')
 otp=2*n*D('.05')+D('2.4')*n*D('.1819')
 cfdi=D(299)+D('.6')*n
 stripe=(D('.043')*1499+3)*n
 ai=AI_PER_USER*n*D(tasks)/20; search=D('.3')*n*D(tasks)/20
 usd=central+VM_PER_USER*n+ai+search+secrets
 tech_net=usd*fx+cfdi/D('1.16'); tech_cash=usd*fx*D('1.16')+cfdi
 provider_net=tech_net+(kyc+otp)*fx+stripe
 provider_cash=tech_cash+((kyc+otp)*fx+stripe)*D('1.16')
 ops=sum(D(r[1][i]) for r in OPS); fraud=10*n
 return dict(n=n,new=new,central_usd=central,secrets_usd=secrets,vm_usd=VM_PER_USER*n,ai_usd=ai,search_usd=search,kyc_usd=kyc,otp_usd=otp,cfdi_gross=cfdi,stripe_net_mxn=stripe,tech_net_mxn=tech_net,tech_cash_mxn=tech_cash,providers_net_mxn=provider_net,providers_cash_mxn=provider_cash,ops_mxn=ops,fraud_reserve_mxn=fraud,all_in_cash_mxn=provider_cash+ops+fraud)
SCENARIOS=[scenario(i) for i in range(3)]
BUILD_LABOR=sum(D(f)*r*m for _,f,r,m in BUILD_TEAM)
BUILD_ONE_OFF=sum(D(v) for _,v in ONE_OFF)
BUILD_TECH=4*SCENARIOS[0]['tech_cash_mxn']
BUILD_SUBTOTAL=BUILD_LABOR+BUILD_ONE_OFF+BUILD_TECH
BUILD_TOTAL=BUILD_SUBTOTAL*D('1.2')
GPU_QWEN_HW=D('1.09')*730+100*D('.07'); GPU_OSS_HW=D('2.89')*730+7
GPU_OPS=D(8000)/FX
FLY_60=D('25.39')/720*60+20*D('.15')+2*D('.15')*660/720+20*D('.08')+10*D('.02')
FLY_720=D('25.39')+20*D('.15')+20*D('.08')+10*D('.02')

def self_check():
 assert AI_PER_USER==D('.5808') and BUILD_LABOR==1660000 and BUILD_ONE_OFF==400000
 assert GPU_QWEN_HW==D('802.70') and GPU_OSS_HW==D('2116.70')
 expected=['114112.0804','242358.2688','1220098.5296']
 for s,e in zip(SCENARIOS,expected): assert s['all_in_cash_mxn']==D(e),(s,e)
 return True
if __name__=='__main__':
 import json
 self_check()
 print(json.dumps(dict(scenarios=SCENARIOS,build_total=BUILD_TOTAL,build_tech=BUILD_TECH,fly_60=FLY_60,fly_720=FLY_720),default=str,indent=2))
