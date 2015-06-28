class Attacker:
	def asuraAddDamage(self, args):#Move on spawn
		dmgper = args[1]
		asureStirkeActive = sm.skillmanager.getmaptemp(self.userid, 'asureStirkeActive')
		skill = sm.skillmanager.getskillname(self.attacker, self.skillnum, self.attacker)
		race = sm.skillmanager.getracename(self.attacker, self.attacker)
		skill2 = sm.skillmanager.getskillname(self.attacker, self.skillnum, self.victim)
		race2 = sm.skillmanager.getracename(self.attacker, self.victim)
		if asureStirkeActive and not wcmd.getdead(self.victim):
			mult = (float(dmgper) / 100)
			dmg = round(float(self.dmg) * float(mult))
			wcmd.damagesm(self.victim,self.attacker,dmg)
			if not self.weapon in 'nova|mag7|xm1014|sawedoff':
				wcmd.tell(self.attacker, skillsstr['multidmg: make'].get_string(wcmd.getlang(self.attacker), **{'dmg':int(dmg), 'racename':race, 'username':wcmd.getname(self.victim), 'skillname':skill}))#TODO replace message
				wcmd.tell(self.victim, skillsstr['multidmg: take'].get_string(wcmd.getlang(self.victim), **{'dmg':int(dmg), 'racename':race2, 'username':wcmd.getname(self.attacker), 'skillname':skill2}))#TODO replace message
				if effect:
					effects.manage(self.victim,str(effect),self.attacker)#TODO add effect

    def vampiric(self, args):
        chance = args[1]
        vampper = args[2]
        effect = args[3]
        immun = sm.skillmanager.getImmun(self.victim, 'vamp') 
        skill = sm.skillmanager.getskillname(self.attacker, self.skillnum, self.attacker)
        race = sm.skillmanager.getracename(self.attacker, self.attacker)
        skill2 = sm.skillmanager.getskillname(self.attacker, self.skillnum, self.victim)
        race2 = sm.skillmanager.getracename(self.attacker, self.victim)
        immunchance = sm.skillmanager.checkchance(immun) if immun else False
        ifchance = sm.skillmanager.checkchance(chance)
    
        if immunchance and ifchance:
            wcmd.tell(self.attacker, skillsstr['leech: imuntake'].get_string(wcmd.getlang(self.attacker), **{'racename':race, 'username':wcmd.getname(self.victim), 'skillname':skill}))
            wcmd.tell(self.victim, skillsstr['leech: imunmake'].get_string(wcmd.getlang(self.victim), **{'racename':race2, 'username':wcmd.getname(self.attacker), 'skillname':skill2}))
        if ifchance and not immunchance and not wcmd.getdead(self.victim) and not immunchance:
            mult = (float(vampper) / 100)
            hp = wcmd.gethealth(self.victim)
            realhp = hp+self.dmg
            heal = round(float(self.dmg * mult)) if self.dmg <= realhp else round(float(realhp * mult))
            wcmd.addhealth(self.attacker, heal)
            if not self.weapon in 'nova|mag7|xm1014|sawedoff':
                wcmd.tell(self.attacker, skillsstr['leech: make'].get_string(wcmd.getlang(self.attacker), **{'hp':int(heal), 'racename':race, 'username':wcmd.getname(self.victim), 'skillname':skill}))
                wcmd.tell(self.victim, skillsstr['leech: take'].get_string(wcmd.getlang(self.victim), **{'hp':int(heal), 'racename':race2, 'username':wcmd.getname(self.attacker), 'skillname':skill2}))
                if effect:
                    effects.manage(self.victim,str(effect),self.attacker)
            
    def freeze(self, args):
        chance = args[1]
        time = args[2]
        effect = args[3]
        immun = sm.skillmanager.getImmun(self.victim, 'freeze')
    
        skill = sm.skillmanager.getskillname(self.attacker, self.skillnum, self.attacker)
        race = sm.skillmanager.getracename(self.attacker, self.attacker)
        skill2 = sm.skillmanager.getskillname(self.attacker, self.skillnum, self.victim)
        race2 = sm.skillmanager.getracename(self.attacker, self.victim)
        immunchance = sm.skillmanager.checkchance(immun) if immun else False
        ifchance = sm.skillmanager.checkchance(chance)
        if immunchance and ifchance:
            wcmd.tell(self.attacker, skillsstr['freeze: imuntake'].get_string(wcmd.getlang(self.attacker), **{'racename':race, 'username':wcmd.getname(self.victim), 'skillname':skill}))
            wcmd.tell(self.victim, skillsstr['freeze: imunmake'].get_string(wcmd.getlang(self.victim), **{'racename':race2, 'username':wcmd.getname(self.attacker), 'skillname':skill2}))

        if ifchance and not wcmd.getfreeze(self.victim) and not wcmd.getdead(self.victim) and not immunchance:
            wcmd.freeze_time(self.victim, float(time))
            if not self.weapon in 'nova|mag7|xm1014|sawedoff':
                wcmd.tell(self.attacker, skillsstr['freeze: make'].get_string(wcmd.getlang(self.attacker), **{'time':float(time), 'racename':race, 'username':wcmd.getname(self.victim), 'skillname':skill}))
                wcmd.tell(self.victim, skillsstr['freeze: take'].get_string(wcmd.getlang(self.victim), **{'time':float(time), 'racename':race2, 'username':wcmd.getname(self.attacker), 'skillname':skill2}))
                if effect:
                    effects.manage(self.victim,str(effect),self.attacker)
            
    def multidmg(self, args):
        if not self.weapon == 'hegrenade':
            chance = args[1]
            dmgper = args[2]
            effect = args[3]
            ifchance = sm.skillmanager.checkchance(chance)
            skill = sm.skillmanager.getskillname(self.attacker, self.skillnum, self.attacker)
            race = sm.skillmanager.getracename(self.attacker, self.attacker)
            skill2 = sm.skillmanager.getskillname(self.attacker, self.skillnum, self.victim)
            race2 = sm.skillmanager.getracename(self.attacker, self.victim)
            if ifchance and not wcmd.getdead(self.victim):
                mult = (float(dmgper) / 100)
                dmg = round(float(self.dmg) * float(mult))
                wcmd.damagesm(self.victim,self.attacker,dmg)
                if not self.weapon in 'nova|mag7|xm1014|sawedoff':
                    wcmd.tell(self.attacker, skillsstr['multidmg: make'].get_string(wcmd.getlang(self.attacker), **{'dmg':int(dmg), 'racename':race, 'username':wcmd.getname(self.victim), 'skillname':skill}))
                    wcmd.tell(self.victim, skillsstr['multidmg: take'].get_string(wcmd.getlang(self.victim), **{'dmg':int(dmg), 'racename':race2, 'username':wcmd.getname(self.attacker), 'skillname':skill2}))
                    if effect:
                        effects.manage(self.victim,str(effect),self.attacker)

    def grenadedmg(self, args):
        print(self.weapon)
        if self.weapon == 'hegrenade':
            chance = 70
            dmgper = args[1]
            effect = args[2]
            ifchance = sm.skillmanager.checkchance(chance)
            skill = sm.skillmanager.getskillname(self.attacker, self.skillnum, self.attacker)
            race = sm.skillmanager.getracename(self.attacker, self.attacker)
            skill2 = sm.skillmanager.getskillname(self.attacker, self.skillnum, self.victim)
            race2 = sm.skillmanager.getracename(self.attacker, self.victim)
            if ifchance and not wcmd.getdead(self.victim):
                mult = (float(dmgper) / 100)
                dmg = round(float(self.dmg) * float(mult))
                wcmd.damagesm(self.victim,self.attacker,dmg)
                if not self.weapon in 'nova|mag7|xm1014|sawedoff':
                    wcmd.tell(self.attacker, skillsstr['multigren: make'].get_string(wcmd.getlang(self.attacker), **{'dmg':int(dmg), 'racename':race, 'username':wcmd.getname(self.victim), 'skillname':skill}))
                    wcmd.tell(self.victim, skillsstr['multigren: take'].get_string(wcmd.getlang(self.victim), **{'dmg':int(dmg), 'racename':race2, 'username':wcmd.getname(self.attacker), 'skillname':skill2}))
                    if effect:
                        effects.manage(self.victim,str(effect),self.attacker)
                
    def drunk(self, args):
        chance = args[1]
        time = args[2]
        effect = args[3]
        immun = sm.skillmanager.getImmun(self.victim, 'drunk')
    
        skill = sm.skillmanager.getskillname(self.attacker, self.skillnum, self.attacker)
        race = sm.skillmanager.getracename(self.attacker, self.attacker)
        skill2 = sm.skillmanager.getskillname(self.attacker, self.skillnum, self.victim)
        race2 = sm.skillmanager.getracename(self.attacker, self.victim)
        immunchance = sm.skillmanager.checkchance(immun) if immun else False
        ifchance = sm.skillmanager.checkchance(chance)
        ifdrunk = sm.skillmanager.isdrug(self.victim)
        if immunchance and ifchance and not ifdrunk:
            wcmd.tell(self.attacker, skillsstr['drunk: imuntake'].get_string(wcmd.getlang(self.attacker), **{'racename':race, 'username':wcmd.getname(self.victim), 'skillname':skill}))
            wcmd.tell(self.victim, skillsstr['drunk: imuntake'].get_string(wcmd.getlang(self.victim), **{'racename':race2, 'username':wcmd.getname(self.attacker), 'skillname':skill2}))

        if ifchance and not wcmd.getdead(self.victim) and not ifdrunk and not immunchance:
            wcmd.drunk(self.victim, 155,float(time))
            if not self.weapon in 'nova|mag7|xm1014|sawedoff':
                wcmd.tell(self.attacker, skillsstr['drunk: make'].get_string(wcmd.getlang(self.attacker), **{'time':float(time), 'racename':race, 'username':wcmd.getname(self.victim), 'skillname':skill}))
                wcmd.tell(self.victim, skillsstr['drunk: take'].get_string(wcmd.getlang(self.victim), **{'time':float(time), 'racename':race2, 'username':wcmd.getname(self.attacker), 'skillname':skill2}))
                if effect:
                    effects.manage(self.victim,str(effect),self.attacker)

    def monsteal(self, args):
        chance = args[1]
        value = int(args[2])
        effect = args[3]
    
        skill = sm.skillmanager.getskillname(self.attacker, self.skillnum, self.attacker)
        race = sm.skillmanager.getracename(self.attacker, self.attacker)
        skill2 = sm.skillmanager.getskillname(self.attacker, self.skillnum, self.victim)
        race2 = sm.skillmanager.getracename(self.attacker, self.victim)
        ifchance = sm.skillmanager.checkchance(chance)
        
        if ifchance and not wcmd.getdead(self.victim):
            enmoney = wcmd.getcash(self.victim)
            money = wcmd.getcash(self.attacker)
            if enmoney >= value:
                wcmd.setcash(self.victim, enmoney - value)
                wcmd.setcash(self.attacker, money + value)
                wcmd.tell(self.attacker, skillsstr['monsteal: make'].get_string(wcmd.getlang(self.attacker), **{'money':value, 'racename':race, 'username':wcmd.getname(self.victim), 'skillname':skill}))
                wcmd.tell(self.victim, skillsstr['monsteal: take'].get_string(wcmd.getlang(self.victim), **{'money':value, 'racename':race2, 'username':wcmd.getname(self.attacker), 'skillname':skill2}))
                if effect:
                    effects.manage(self.victim,str(effect),self.attacker)
            elif enmoney > 0:
                wcmd.setcash(self.victim, 0)
                wcmd.setcash(self.attacker, money + enmoney)
                if not self.weapon in 'nova|mag7|xm1014|sawedoff':
                    wcmd.tell(self.attacker, skillsstr['monsteal: make'].get_string(wcmd.getlang(self.attacker), **{'money':value, 'racename':race, 'username':wcmd.getname(self.victim), 'skillname':skill}))
                    wcmd.tell(self.victim, skillsstr['monsteal: take'].get_string(wcmd.getlang(self.victim), **{'money':value, 'racename':race2, 'username':wcmd.getname(self.attacker), 'skillname':skill2}))
                    if effect:
                        effects.manage(self.victim,str(effect),self.attacker)
                
    def burn(self, args):
        chance = args[1]
        time = args[2]
        effect = args[3]
        immun = sm.skillmanager.getImmun(self.victim, 'burn')
    
        skill = sm.skillmanager.getskillname(self.attacker, self.skillnum, self.attacker)
        race = sm.skillmanager.getracename(self.attacker, self.attacker)
        skill2 = sm.skillmanager.getskillname(self.attacker, self.skillnum, self.victim)
        race2 = sm.skillmanager.getracename(self.attacker, self.victim)
        immunchance = sm.skillmanager.checkchance(immun) if immun else False
        ifchance = sm.skillmanager.checkchance(chance)
        ifburn = sm.skillmanager.isburn(self.victim)
        if immunchance and ifchance and not ifburn:
            wcmd.tell(self.attacker, skillsstr['burn: imuntake'].get_string(wcmd.getlang(self.attacker), **{'racename':race, 'username':wcmd.getname(self.victim), 'skillname':skill}))
            wcmd.tell(self.victim, skillsstr['burn: imuntake'].get_string(wcmd.getlang(self.victim), **{'racename':race2, 'username':wcmd.getname(self.attacker), 'skillname':skill2}))

        if ifchance and not wcmd.getdead(self.victim) and not ifburn and not immunchance:
            wcmd.burn(self.victim, self.attacker, float(time))
            if not self.weapon in 'nova|mag7|xm1014|sawedoff':
                wcmd.tell(self.attacker, skillsstr['burn: make'].get_string(wcmd.getlang(self.attacker), **{'time':float(time), 'racename':race, 'username':wcmd.getname(self.victim), 'skillname':skill}))
                wcmd.tell(self.victim, skillsstr['burn: take'].get_string(wcmd.getlang(self.victim), **{'time':float(time), 'racename':race2, 'username':wcmd.getname(self.attacker), 'skillname':skill2}))
                if effect:
                    effects.manage(self.victim,str(effect),self.attacker)

    def teamleech(self, args):
        chance = args[1]
        effect = args[2]
        immun = sm.skillmanager.getImmun(self.victim, 'vamp') 
        skill = sm.skillmanager.getskillname(self.attacker, self.skillnum, self.attacker)
        race = sm.skillmanager.getracename(self.attacker, self.attacker)
        skill2 = sm.skillmanager.getskillname(self.attacker, self.skillnum, self.victim)
        race2 = sm.skillmanager.getracename(self.attacker, self.victim)
        immunchance = sm.skillmanager.checkchance(immun) if immun else False
        ifchance = sm.skillmanager.checkchance(chance)
    
        if immunchance and ifchance:
            wcmd.tell(self.attacker, skillsstr['leech: imuntake'].get_string(wcmd.getlang(self.attacker), **{'racename':race, 'username':wcmd.getname(self.victim), 'skillname':skill}))
            wcmd.tell(self.victim, skillsstr['leech: imunmake'].get_string(wcmd.getlang(self.victim), **{'racename':race2, 'username':wcmd.getname(self.attacker), 'skillname':skill2}))
        if ifchance and not immunchance and not wcmd.getdead(self.victim) and not immunchance:
            hp = int(self.dmg)*0.3
            if not self.weapon in 'nova|mag7|xm1014|sawedoff':
                wcmd.tell(self.attacker, skillsstr['teamleech: make'].get_string(wcmd.getlang(self.attacker), **{'hp':int(self.dmg), 'racename':race, 'username':wcmd.getname(self.victim), 'skillname':skill}))
                wcmd.tell(self.victim, skillsstr['teamleech: take'].get_string(wcmd.getlang(self.victim), **{'hp':int(self.dmg), 'racename':race2, 'username':wcmd.getname(self.attacker), 'skillname':skill2}))
            for user in wcmd.getUseridList_filter(['alive']+[['t','ct'][wcmd.getplayerteam(self.attacker)-2]]):
                if not user == self.attacker:
                    skill3 = sm.skillmanager.getskillname(self.attacker, self.skillnum, user)
                    race3 = sm.skillmanager.getracename(self.attacker, user)
                    wcmd.addhealth(user, int(hp))
                    wcmd.tell(user, skillsstr['teamleech: take2'].get_string(wcmd.getlang(self.victim), **{'hp':int(hp), 'racename':race3, 'username':wcmd.getname(self.attacker), 'skillname':skill2}))
					
					
					
					
class Kill:
    def __init__(self,event):
        self.victim = event[0]
        self.attacker = event[1]
        self.weapon = event[2]
        self.skillnum = event[3]
        
    def damageteam(self, args):
        chance = args[1]
        dmg = args[2]
        ownername = wcmd.getname(self.attacker)
        ifchance = sm.skillmanager.checkchance(chance)
        skill1 = sm.skillmanager.getskillname(self.attacker, self.skillnum, self.attacker)
        race1 = sm.skillmanager.getracename(self.attacker, self.attacker)       
        if ifchance:
            wcmd.tell(self.attacker, skillsstr['damageteam: make'].get_string(wcmd.getlang(self.attacker), **{'dmg':int(dmg), 'racename':race1, 'skillname':skill1}))
            for user in wcmd.getUseridList_filter(['alive']+[['ct','t'][wcmd.getplayerteam(self.attacker)-2]]):
                if not self.attacker == user:
                    skill = sm.skillmanager.getskillname(self.attacker, self.skillnum, user)
                    race = sm.skillmanager.getracename(self.attacker, user)
                    regenable = sm.skillmanager.gettemp(user, 'notregenable')
                    if not regenable:         
                        wcmd.damagesm(user, self.attacker, int(dmg),'wcs_teamdamage')
                        wcmd.tell(user, skillsstr['damageteam: take'].get_string(wcmd.getlang(self.attacker), **{'dmg':int(dmg), 'racename':race1, 'skillname':skill1, 'username':ownername}))
						
	def addSphere(self, args):#TODO add this skill from on spawn
		maxsphere = args[1]
		spheresCount = sm.skillmanager.getmaptemp(self.userid, 'spheresCount')
		if spheresCount < maxsphere :
			 sm.skillmanager.setmaptemp(self.attacker, 'spheresCount', spheresCount+1)
			 wcmd.tell(user, skillsstr['damageteam: take'].get_string(wcmd.getlang(self.attacker), **{'dmg':int(dmg), 'racename':race1, 'skillname':skill1, 'username':ownername}))#TODO Replace messages
		else:
			wcmd.tell(user, skillsstr['damageteam: take'].get_string(wcmd.getlang(self.attacker), **{'dmg':int(dmg), 'racename':race1, 'skillname':skill1, 'username':ownername}))#TODO Replace message
                    
class Spawn:
    def __init__(self,event):
        self.userid = event[0]
        self.skillnum = event[1]
        
    def speed(self, args):
        value = args[1]
        wcmd.setspeed(self.userid, value)
        race = sm.skillmanager.getracename(self.userid, self.userid)
        wcmd.tell(self.userid, skillsstr['speed'].get_string(wcmd.getlang(self.userid), **{'speed':value, 'racename':race}))
		
    def speedMonk(self, args):
        value = args[1]
        wcmd.setspeed(self.userid, value)
        race = sm.skillmanager.getracename(self.userid, self.userid)
        wcmd.tell(self.userid, skillsstr['speed'].get_string(wcmd.getlang(self.userid), **{'speed':value, 'racename':race}))
		sm.skillmanager.manage(self.userid, 'victim_decreaseByDistance', str(self.skillnum)+'_100')#TODO check params
    
    def levitation(self, args):
        value = args[1]
        wcmd.setgravity(self.userid, value)
        race = sm.skillmanager.getracename(self.userid, self.userid)
        wcmd.tell(self.userid, skillsstr['gravity'].get_string(wcmd.getlang(self.userid), **{'grav':value, 'racename':race}))
    
    def health(self, args):
        value = args[1]
        wcmd.addhealth(self.userid, value)
        race = sm.skillmanager.getracename(self.userid, self.userid)
        wcmd.tell(self.userid, skillsstr['health'].get_string(wcmd.getlang(self.userid), **{'health':value, 'racename':race}))	

	def speferesDamage(self, args):
        spheresMaxCount = args[1]
        spheresDamage = args[2]
        delay = args[3]
        radius = args[4]
		if wcmd.getplayerteam(self.userid) >= 2:
            if wcmd.getUseridList_filter('alive'):
				sm.skillmanager.delayed['speferesDamage_'+str(self.userid)] = tick_delays.delay(time, speferesDamage, self.userid, delay, prm1, prm2)#TODO what is prm1, prm2
                x,y,z = wcmd.getlocation(self.userid)       
                for user in wcmd.getUseridList_filter(['alive']+[['ct','t'][wcmd.getplayerteam(self.userid)-2]]):
                    x1,y1,z1 = wcmd.getlocation(user)
					spheresCount = sm.skillmanager.getmaptemp(self.userid, 'spheresCount')
					dmg = spheresCount*spheresDamage
                    if ((x1 - x) ** 2 + (y1 - y) ** 2 + (z1 - z) ** 2) ** 0.5 <= float(radius):
						if sm.skillmanager.getImmun(user, 'periodicallyDamage'):
                            wcmd.tell(user, skillsstr['ultimun: make'].get_string(wcmd.getlang(user), **{'racename':race, 'username':wcmd.getname(self.userid)}))#TODO Replace message
                            wcmd.tell(self.userid, skillsstr['ultimun: take'].get_string(wcmd.getlang(self.userid), **{'racename':race, 'username':wcmd.getname(user), 'skillname':skill}))#TODO Replace message
                        else:
                            skill2 = sm.skillmanager.getskillname(self.userid, self.skillnum, user)
                            race2 = sm.skillmanager.getracename(self.userid, user)
                            wcmd.damagesm(user,self.userid,int(dmg),'wcs_spheredamage')
                            count += 1
                            wcmd.tell(user, skillsstr['multidmg: take'].get_string(wcmd.getlang(user), **{'dmg':int(dmg), 'racename':race2, 'username':wcmd.getname(self.userid), 'skillname':skill2}))#TODO Replace message
                            if effect:
                                effects.manage(user,str(effect),self.userid)	#TODO Add effect
		
class Victim:
    def __init__(self,event):
        self.victim = event[0]
        self.attacker = event[1]
        self.dmg = event[2]
        self.weapon = event[3]
        self.skillnum = event[4]
        
    def mirrowdmg(self, args):
        chance = args[1]
        dmgper = args[2]
        effect = args[3]
        ifchance = sm.skillmanager.checkchance(chance)
        regenable = sm.skillmanager.gettemp(self.attacker, 'notregenable')
        if ifchance and not wcmd.getdead(self.victim) and not regenable:
            mult = (float(dmgper) / 100)
            dmg = round(float(self.dmg) * float(mult))
            wcmd.damagesm(self.attacker,self.victim,dmg,'wcs_mirrowdamage')
       
            skill = sm.skillmanager.getskillname(self.victim, self.skillnum, self.victim)
            race = sm.skillmanager.getracename(self.victim, self.victim)
            skill2 = sm.skillmanager.getskillname(self.victim, self.skillnum, self.attacker)
            race2 = sm.skillmanager.getracename(self.victim, self.attacker)
            if not self.weapon in 'nova|mag7|xm1014|sawedoff':
                wcmd.tell(self.victim, skillsstr['mirrordmg: make'].get_string(wcmd.getlang(self.victim), **{'dmg':int(dmg), 'racename':race, 'username':wcmd.getname(self.attacker), 'skillname':skill}))
                wcmd.tell(self.attacker, skillsstr['mirrordmg: take'].get_string(wcmd.getlang(self.attacker), **{'dmg':int(dmg), 'racename':race2, 'username':wcmd.getname(self.victim), 'skillname':skill2}))
	#Mefodil's			TODO Move to another event on pre damage
    def decreaseByDistance(self, args):   
        percent = args[2]
        radius = args[1]
		mult = (float(percent) / 100)	
		x,y,z = wcmd.getlocation(self.victim) 
		x1,y1,z1 = wcmd.getlocation(self.attacker)		
		if ((x1 - x) ** 2 + (y1 - y) ** 2 + (z1 - z) ** 2) ** 0.5 <= float(radius): # if attacker in radius of skill
			newDamage  = int(self.dmg * mult) # decrease incoming damage
			self.dmg = newDamage
			#TODO section inform about this effect
            skill = sm.skillmanager.getskillname(self.victim, self.skillnum, self.victim)
            race = sm.skillmanager.getracename(self.victim, self.victim)
            skill2 = sm.skillmanager.getskillname(self.victim, self.skillnum, self.attacker)
            race2 = sm.skillmanager.getracename(self.victim, self.attacker)
            if not self.weapon in 'nova|mag7|xm1014|sawedoff':
				wcmd.tell(self.victim, skillsstr['mirrordmg: make'].get_string(wcmd.getlang(self.victim), **{'dmg':int(dmg), 'racename':race, 'username':wcmd.getname(self.attacker), 'skillname':skill}))#TODO Replace message
				wcmd.tell(self.attacker, skillsstr['mirrordmg: take'].get_string(wcmd.getlang(self.attacker), **{'dmg':int(dmg), 'racename':race2, 'username':wcmd.getname(self.victim), 'skillname':skill2}))#TODO Replace message




	
#Mefodil's			
class Ability:
    def __init__(self,event):
        self.userid = event[0]
        self.skillnum = event[1]		
	
	def teleportationW3S(self, args):
		if wcmd.getplayerteam(self.userid) >= 2:
			if not wcmd.getdead(self.userid):
				self.userid.teleport(None, None, velocity_cector);
				if is_player_stuck(self.userid): #TODO check name of function
			
				
class Ultimate:
    def __init__(self,event):
        self.userid = event[0]
        self.skillnum = event[1]
            
    def asuraStirkeUse(self, args):
		spheresCount = sm.skillmanager.getmaptemp(self.userid, 'spheresCount')
		if spheresCount > 0 :
			sm.skillmanager.setmaptemp(self.attacker, 'spheresCount', spheresCount-1)
			sm.skillmanager.settemp(self.userid, 'asureStirkeActive', true)
			wcmd.tell(user, skillsstr['multidmg: take'].get_string(wcmd.getlang(user), **{'dmg':int(dmg), 'racename':race2, 'username':wcmd.getname(self.userid), 'skillname':skill2}))#TODO replace message
		else:
			wcmd.tell(user, skillsstr['multidmg: take'].get_string(wcmd.getlang(user), **{'dmg':int(dmg), 'racename':race2, 'username':wcmd.getname(self.userid), 'skillname':skill2}))#TODO replace message
    def chain(self, args):
        radius = args[1]
        dmg = args[2]
        effect = args[3]
        count = 0
        skill = sm.skillmanager.getskillname(self.userid, self.skillnum, self.userid)
        race = sm.skillmanager.getracename(self.userid, self.userid)
        if wcmd.getplayerteam(self.userid) >= 2:
            if wcmd.getUseridList_filter('alive'):
                x,y,z = wcmd.getlocation(self.userid)       
                for user in wcmd.getUseridList_filter(['alive']+[['ct','t'][wcmd.getplayerteam(self.userid)-2]]):
                    x1,y1,z1 = wcmd.getlocation(user)
                    if ((x1 - x) ** 2 + (y1 - y) ** 2 + (z1 - z) ** 2) ** 0.5 <= float(radius):
                        if sm.skillmanager.getImmun(user, 'ulti'):
                            wcmd.tell(user, skillsstr['ultimun: make'].get_string(wcmd.getlang(user), **{'racename':race, 'username':wcmd.getname(self.userid)}))
                            wcmd.tell(self.userid, skillsstr['ultimun: take'].get_string(wcmd.getlang(self.userid), **{'racename':race, 'username':wcmd.getname(user), 'skillname':skill}))
                        else:
                            skill2 = sm.skillmanager.getskillname(self.userid, self.skillnum, user)
                            race2 = sm.skillmanager.getracename(self.userid, user)
                            wcmd.damagesm(user,self.userid,int(dmg),'wcs_chaindamage')
                            count += 1
                            wcmd.tell(user, skillsstr['multidmg: take'].get_string(wcmd.getlang(user), **{'dmg':int(dmg), 'racename':race2, 'username':wcmd.getname(self.userid), 'skillname':skill2}))
                            if effect:
                                effects.manage(user,str(effect),self.userid)

        if count:   
            wcmd.tell(self.userid, skillsstr['chainlight: done'].get_string(wcmd.getlang(self.userid), **{'count':int(count), 'racename':race, 'skillname':skill, 'dmg':dmg}))
        else:
            wcmd.tell(self.userid, skillsstr['rangefail'].get_string(wcmd.getlang(self.userid), **{'racename':race, 'skillname':skill}))
            cancel(self.userid, 'player_ultimate')
            
    def roots(self, args):
        radius = args[1]
        time = args[2]
        effect = args[3]
        count = 0
        skill = sm.skillmanager.getskillname(self.userid, self.skillnum, self.userid)
        race = sm.skillmanager.getracename(self.userid, self.userid)
        if wcmd.getplayerteam(self.userid) >= 2:
            if wcmd.getUseridList_filter('alive'):
                x,y,z = wcmd.getlocation(self.userid)       
                for user in wcmd.getUseridList_filter(['alive']+[['ct','t'][wcmd.getplayerteam(self.userid)-2]]):
                    x1,y1,z1 = wcmd.getlocation(user)
                    if ((x1 - x) ** 2 + (y1 - y) ** 2 + (z1 - z) ** 2) ** 0.5 <= float(radius):
                        if sm.skillmanager.getImmun(user, 'ulti'):
                            wcmd.tell(user, skillsstr['ultimun: make'].get_string(wcmd.getlang(user), **{'racename':race, 'username':wcmd.getname(self.userid)}))
                            wcmd.tell(self.userid, skillsstr['ultimun: take'].get_string(wcmd.getlang(self.userid), **{'racename':race, 'username':wcmd.getname(user), 'skillname':skill}))
                        else:
                            skill2 = sm.skillmanager.getskillname(self.userid, self.skillnum, user)
                            race2 = sm.skillmanager.getracename(self.userid, user)
                            wcmd.freeze_time(user, float(time))
                            count += 1
                            wcmd.tell(user, skillsstr['roots: take'].get_string(wcmd.getlang(user), **{'time':float(time), 'racename':race2, 'username':wcmd.getname(self.userid), 'skillname':skill2}))
                            if effect:
                                effects.manage(user,str(effect),self.userid)

        if count:   
            wcmd.tell(self.userid, skillsstr['roots: done'].get_string(wcmd.getlang(self.userid), **{'count':int(count), 'racename':race, 'skillname':skill, 'time':float(time)}))
        else:
            wcmd.tell(self.userid, skillsstr['rangefail'].get_string(wcmd.getlang(self.userid), **{'racename':race, 'skillname':skill}))
            cancel(self.userid, 'player_ultimate')