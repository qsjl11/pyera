# -*- coding: UTF-8 -*-
import core.cfg

core.cfg.platform = 'web'

import core.io as io
import core.flow
import core.data
import script.mainflow


#############################################################
io.run(script.mainflow.open_func)

