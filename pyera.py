# -*- coding: UTF-8 -*-
import core.cfg

core.cfg.platform = 'win'
import core.winframe
import core.io
import core.flow
import core.data
import script.mainflow

core.winframe.run(core.flow.get_flow('open_flow'))
