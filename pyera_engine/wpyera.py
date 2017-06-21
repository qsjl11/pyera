# -*- coding: UTF-8 -*-
import core.cfg

core.cfg.platform = 'web'

import core.game
import script.mainflow

core.game.run(script.mainflow.open_func)
