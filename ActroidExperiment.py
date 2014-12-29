#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file ActroidExperiment.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
actroidexperiment_spec = ["implementation_id", "ActroidExperiment", 
		 "type_name",         "ActroidExperiment", 
		 "description",       "ModuleDescription", 
		 "version",           "1.0.0", 
		 "vendor",            "VenderName", 
		 "category",          "Category", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class ActroidExperiment
# @brief ModuleDescription
# 
# 
class ActroidExperiment(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_target = RTC.TimedDoubleSeq(RTC.Time(0,0),[])
		"""
		"""
		self._targetOut = OpenRTM_aist.OutPort("target", self._d_target)


		


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		
		# Set InPort buffers
		
		# Set OutPort buffers
		self.addOutPort("target",self._targetOut)
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The activated action (Active state entry action)
		# former rtc_active_entry()
		#
		# @param ec_id target ExecutionContext Id
		# 
		# @return RTC::ReturnCode_t
		#
		#
	def onActivated(self, ec_id):
                self.time1 = time.time()
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The deactivated action (Active state exit action)
	#	# former rtc_active_exit()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onDeactivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The execution action that is invoked periodically
		# former rtc_active_do()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onExecute(self, ec_id):
                data_array1 = []
                data_array2 = []
                try:
                        global frames
                        self.time2 = time.time()

                        delta_time = int(self.time2-self.time1) #文字列を数値に変換

                        if delta_time < 10:
                                frames1 = [150,150,128,128,0,0,200,0,
                                           40,#L1
                                           25,#L2
                                           0,#L3
                                           3,#L4
                                           0,#L5
                                           -6,#L6
                                           -15,#L7
                                           130,#R1
                                           50,#R2
                                           0,#R3
                                           0,#R4
                                           -90,#R5
                                           0,0,255,155]#初期値
                                x = 0.0174 #532925 #[deg]にこの値をかけたら[rad]に変換できる
                        
                                for num in range(0, 24):
                                        value = frames1[num]
                                        data_array1.append(value*x) #[deg]から[rad]に変換
                                self._d_target.data = data_array1
                                self._targetOut.write()
                                self._targetOut._updated = True
                        
                        else:
                                frames2 = [150,150,128,128,0,0,200,0,
                                           40,#L1(-14-300)
                                           25,#L2(0-57)
                                           0,#L3(0-90)
                                           0,#L4(0-112)
                                           0,#L5(-90-90)
                                           -6,#L6(-40-28)
                                           26,#L7(-15-26)
                                           130,#R1(-14-130)
                                           50,#R2(0-57)
                                           0,#R3(0-90)
                                           0,#R4(0-112)
                                           -90,#R5(-90-90)
                                           0,0,255,155]#目標値
                                x = 0.0174 #532925 #[deg]にこの値をかけたら[rad]に変換できる
                        
                                for num in range(0, 24):
                                        value = frames2[num]
                                        data_array2.append(value*x) #[deg]から[rad]に変換
                                self._d_target.data = data_array2
                                self._targetOut.write()
                                self._targetOut._updated = True

                        #self._d_target.tm = delta_time
                        #self._targetOut.write()
                        #print self._d_target.tm

                        #self._targetOut._updated = True

                        #if self._targetOut._updated == True:
                        #        print "stop"

	
                        return RTC.RTC_OK

                except Exception, e:
                        print 'Exception : ', e
                        pass
	
		return RTC.RTC_OK
	
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def ActroidExperimentInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=actroidexperiment_spec)
    manager.registerFactory(profile,
                            ActroidExperiment,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    ActroidExperimentInit(manager)

    # Create a component
    comp = manager.createComponent("ActroidExperiment")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

