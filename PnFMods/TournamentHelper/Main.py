API_VERSION = 'API_v1.0'
MOD_NAME = 'TournamentHelper'

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
#
IS_TOURNAMENT_ENABLED = True

# WMI 2025
SHIP_DATA = {
    3550361328: {'weight':  12, 'isFlagship': False}, # Alberico da Barbiano     , PISD710 
    4074681808: {'weight':  22, 'isFlagship': False}, # Alexander Nevsky         , PRSC210 
    3760076208: {'weight':  14, 'isFlagship': False}, # Álvaro de Bazán          , PSSD510 
    4179506928: {'weight':  10, 'isFlagship': False}, # Attilio Regolo           , PISD110 
    3445536752: {'weight':   9, 'isFlagship': False}, # Austin                   , PASC810 
    3760142160: {'weight':  19, 'isFlagship': False}, # Bourgogne                , PFSB510 
    3550394192: {'weight':  12, 'isFlagship': False}, # Brennus                  , PFSC710 
    3760108912: {'weight':  20, 'isFlagship': False}, # Brisbane                 , PUSC510 
    4074714832: {'weight':  20, 'isFlagship': False}, # Bungo                    , PJSB210 
    4284364624: {'weight':  13, 'isFlagship': False}, # Cassard                  , PFSD010 
    4179539376: {'weight':  12, 'isFlagship': False}, # Castilla                 , PSSC110 
    4284396912: {'weight':  14, 'isFlagship': False}, # Cerberus                 , PUSC010 
    3760109392: {'weight':  10, 'isFlagship': False}, # Colbert                  , PFSC510 
    4179572688: {'weight':  19, 'isFlagship': False}, # Conqueror                , PBSB110 
    4179572464: {'weight':  28, 'isFlagship': False}, # Cristoforo Colombo       , PISB110 
    4179507152: {'weight':  13, 'isFlagship': False}, # Daring                   , PBSD110 
    3445536720: {'weight':  12, 'isFlagship': False}, # Defence                  , PBSC810 
    3864933840: {'weight':  14, 'isFlagship': False}, # Delny                    , PRSD410 
    4273911792: {'weight':  19, 'isFlagship': False}, # Des Moines               , PASC020 
    3760076752: {'weight':  11, 'isFlagship': False}, # Druid                    , PBSD510 
    4074649392: {'weight':  13, 'isFlagship': False}, # Elbing                   , PGSD210 
    3655219184: {'weight':  17, 'isFlagship': False}, # Forrest Sherman          , PASD610 
    4074648880: {'weight':  19, 'isFlagship': False}, # Gdańsk                   , PWSD210 
    4281219056: {'weight':  18, 'isFlagship': False}, # Gearing                  , PASD013 
    3550361392: {'weight':  13, 'isFlagship': False}, # Georg Hoffmann           , PGSD710 
    3655251920: {'weight':  12, 'isFlagship': False}, # Gibraltar                , PBSC610 
    4074682320: {'weight':  14, 'isFlagship': False}, # Goliath                  , PBSC210 
    4179539728: {'weight':  11, 'isFlagship': False}, # Gouden Leeuw             , PHSC110 
    4179572528: {'weight':  17, 'isFlagship': False}, # Grosser Kurfürst         , PGSB110 
    4074649040: {'weight':  14, 'isFlagship': False}, # Grozovoi                 , PRSD210 
    4179506480: {'weight':  12, 'isFlagship': False}, # Halland                  , PWSD110 
    4074649296: {'weight':  19, 'isFlagship': False}, # Harugumo                 , PJSD210 
    3760076496: {'weight':  14, 'isFlagship': False}, # Hayate                   , PJSD510 
    4179539792: {'weight':  12, 'isFlagship': False}, # Henri IV                 , PFSC110 
    3550394160: {'weight':  27, 'isFlagship': False}, # Hildebrand               , PGSC710 
    4179539760: {'weight':  11, 'isFlagship': False}, # Hindenburg               , PGSC110 
    3539875824: {'weight':  13, 'isFlagship': False}, # Hull                     , PASD720 
    3550393552: {'weight':  14, 'isFlagship': False}, # Incheon                  , PZSC710 
    3655284688: {'weight':  19, 'isFlagship': False}, # Incomparable             , PBSB610 
    3550426480: {'weight':  18, 'isFlagship': False}, # Irresistible             , PUSB710 
    4179539152: {'weight':  14, 'isFlagship': False}, # Jinan                    , PZSC110 
    4179506640: {'weight':  14, 'isFlagship': False}, # Khabarovsk               , PRSD110 
    3655251664: {'weight':   8, 'isFlagship': False}, # Kitakami                 , PJSC610 
    4179507024: {'weight':  16, 'isFlagship': False}, # Kléber                   , PFSD110 
    3445536208: {'weight':  24, 'isFlagship': False}, # Komissar                 , PRSC810 
    4179572176: {'weight':  20, 'isFlagship': False}, # Kremlin                  , PRSB110 
    3550360912: {'weight':  14, 'isFlagship': False}, # La Pampa                 , PVSD710 
    4284429648: {'weight':  23, 'isFlagship': False}, # Libertad                 , PVSB010 
    4074715120: {'weight':  26, 'isFlagship': False}, # Louisiana                , PASB210 
    3760075984: {'weight':  14, 'isFlagship': False}, # Lüshun                   , PZSD510 
    4074649424: {'weight':  16, 'isFlagship': False}, # Marceau                  , PFSD210 
    4074682192: {'weight':  17, 'isFlagship': False}, # Marseille                , PFSC210 
    3655284528: {'weight':  18, 'isFlagship': False}, # Mecklenburg              , PGSB610 
    4179539920: {'weight':  19, 'isFlagship': False}, # Minotaur                 , PBSC110 
    4273911760: {'weight':  13, 'isFlagship': False}, # Monmouth                 , PBSC020 
    4277090288: {'weight':  19, 'isFlagship': False}, # Montana                  , PASB017 
    4179539408: {'weight':  21, 'isFlagship': False}, # Moskva                   , PRSC110 
    3760109296: {'weight':  17, 'isFlagship': False}, # Napoli                   , PISC510 
    3760142320: {'weight':  22, 'isFlagship': False}, # Ohio                     , PASB510 
    3969824208: {'weight':  20, 'isFlagship': False}, # Petropavlovsk            , PRSC310 
    3760109520: {'weight':  15, 'isFlagship': False}, # Plymouth                 , PBSC510 
    3969857328: {'weight':  17, 'isFlagship': False}, # Preussen                 , PGSB310 
    3550394128: {'weight':  13, 'isFlagship': False}, # Prins van Oranje         , PHSC710 
    3655251952: {'weight':  15, 'isFlagship': False}, # Puerto Rico              , PASC610 
    3550360880: {'weight':  17, 'isFlagship': False}, # Ragnar                   , PWSD710 
    4179572560: {'weight':  17, 'isFlagship': False}, # République               , PFSB110 
    3539941360: {'weight':  19, 'isFlagship': False}, # Rhode Island             , PASB720 
    3760142064: {'weight':  21, 'isFlagship': False}, # Ruggiero di Lauria       , PISB510 
    3550394352: {'weight':  17, 'isFlagship': False}, # Salem                    , PASC710 
    4179539280: {'weight':  17, 'isFlagship': False}, # San Martín               , PVSC110 
    4074714928: {'weight':  21, 'isFlagship': False}, # Schlieffen               , PGSB210 
    3550393808: {'weight':  12, 'isFlagship': False}, # Sevastopol               , PRSC710 
    3760142032: {'weight':  18, 'isFlagship': False}, # Shikishima               , PJSB510 
    4282267344: {'weight':  15, 'isFlagship': False}, # Shimakaze                , PJSD012 
    3550426864: {'weight':  17, 'isFlagship': False}, # Sicilia                  , PISB710 
    3760141776: {'weight':  17, 'isFlagship': False}, # Slava                    , PRSB510 
    3655218480: {'weight':  17, 'isFlagship': False}, # Småland                  , PWSD610 
    3655251408: {'weight':  16, 'isFlagship': False}, # Smolensk                 , PRSC610 
    3760076784: {'weight':  18, 'isFlagship': False}, # Somers                   , PASD510 
    4074715088: {'weight':  21, 'isFlagship': False}, # St. Vincent              , PBSB210 
    3760109008: {'weight':  17, 'isFlagship': False}, # Stalingrad               , PRSC510 
    3550393648: {'weight':  19, 'isFlagship': False}, # Svea                     , PWSC710 
    3760142288: {'weight':  21, 'isFlagship': False}, # Thunderer                , PBSB510 
    3655218960: {'weight':  11, 'isFlagship': False}, # Tromp                    , PHSD610 
    4284397328: {'weight':  18, 'isFlagship': False}, # Utrecht                  , PHSC010 
    3760076144: {'weight':  12, 'isFlagship': False}, # Vampire II               , PUSD510 
    4179539696: {'weight':  13, 'isFlagship': False}, # Venezia                  , PISC110 
    4179572720: {'weight':  25, 'isFlagship': False}, # Vermont                  , PASB110 
    3550426896: {'weight':  19, 'isFlagship': False}, # Willem de Eerste         , PHSB710 
    3529455600: {'weight':  22, 'isFlagship': False}, # Wisconsin                , PASB730 
    4074682352: {'weight':  18, 'isFlagship': False}, # Worcester                , PASC210 
    4276041424: {'weight':  18, 'isFlagship': False}, # Yamato                   , PJSB018 
    4074682064: {'weight':  11, 'isFlagship': False}, # Yodo                     , PJSC210 
    3749623504: {'weight':  11, 'isFlagship': False}, # Yoshino                  , PJSC520 
    4179506384: {'weight':  18, 'isFlagship': False}, # Yueyang                  , PZSD110 
    3655218992: {'weight':  13, 'isFlagship': False}, # Z-42                     , PGSD610 
    4179506992: {'weight':  13, 'isFlagship': False}, # Z-52                     , PGSD110 
    4259231440: {'weight':  11, 'isFlagship': False}, # Zaō                      , PJSC034 
}
#
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------


try:
    import events, ui, utils, dataHub, constants, battle, callbacks
except:
    pass

from EntityController import EntityController

CC = constants.UiComponents

SHIP_WEIGHT_KEY_BASE = 'modTournamentShipWeight_{}'
TEAM_WEIGHT_KEY_BASE = 'modTournamentTeamWeight_{}'
TOURNAMENT_MODE_KEY = 'modTournamentMode'

def logInfo(*args):
    data = [str(i) for i in args]
    utils.logInfo( '[{}] {}'.format(MOD_NAME, ', '.join(data)) )

def logError(*args):
    data = [str(i) for i in args]
    utils.logError( '[{}] {}'.format(MOD_NAME, ', '.join(data)) )

class TournamentHelper(object):
    def __init__(self):
        if not IS_TOURNAMENT_ENABLED:
            logInfo('Tournament Mode is disabled. Skipping')
            return
        logInfo('Tournament Mode is enabled. Processing...')
        entityId = ui.createUiElement()
        ui.addDataComponentWithId(entityId, TOURNAMENT_MODE_KEY, {'isTournamentMode': True})

        self.shipWeights = TournamentShipWeight()


class TournamentShipWeight(object):
    def __init__(self, *args):
        for shipId, data in SHIP_DATA.items():
            newEntityId = ui.createUiElement()
            key = SHIP_WEIGHT_KEY_BASE.format(shipId)
            weight = data.get('weight', 0)
            isFlagship = data.get('isFlagship', False)
            ui.addDataComponentWithId(newEntityId, key, {'weight': weight, 'isFlagship': isFlagship})
        logInfo('Added ship weight data', len(SHIP_DATA))

        self._teamWeightEntities = {}
        for teamId in range(2):
            entityId = ui.createUiElement()
            key = TEAM_WEIGHT_KEY_BASE.format(teamId)
            ui.addDataComponentWithId(entityId, key, {'weight': 0})
            self._teamWeightEntities[teamId] = entityId
        events.onSFMEvent(self.__onSFMEevent)
        logInfo('Added team weight entities')

        self._vary = None

    def __onSFMEevent(self, eventName, eventData):
        if eventName == 'window.show' and isinstance(eventData, dict) and eventData.get('windowName', None) == 'ModalWindowTrainingRoom':
            self.__startVary()
        elif eventName == 'action.leaveTrainingRoom':
            self.__stopVary()

    def __startVary(self):
        if self._vary is not None:
            self.__stopVary()
        self._vary = callbacks.perTick(self.recalcTeamWeight)

    def __stopVary(self):
        callbacks.cancel(self._vary)
        self._vary = None

    def recalcTeamWeight(self, *args):
        myAccount = dataHub.getSingleEntity('accountSelf')
        currentPreBattleId = myAccount[CC.preBattlePlayerSimple].preBattleId if CC.preBattlePlayerSimple in myAccount else None
        teamWeights = {0: 0, 1: 0}
        if currentPreBattleId is not None:
            for playerEntity in dataHub.getEntityCollections('preBattlePlayerSimple'):
                preBattlePlayer = playerEntity[CC.preBattlePlayerSimple]
                if preBattlePlayer.preBattleId != currentPreBattleId:
                    continue
                elif preBattlePlayer.shipId is None:
                    continue
                elif preBattlePlayer.teamId not in teamWeights:
                    continue
                else:
                    weight = SHIP_DATA.get(preBattlePlayer.shipId, 0)
                    teamWeights[preBattlePlayer.teamId] += weight.get('weight', 0)

        for teamId, weight in teamWeights.items():
            entityId = self._teamWeightEntities[teamId]
            ui.updateUiElementData(entityId, {'weight': weight})


gHelper = TournamentHelper()