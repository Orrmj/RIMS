import sys
import datetime
import math
from numpy import mat, result_type
from numpy.lib.histograms import _hist_bin_auto
import pandas as pd
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class Signals(qtc.QObject):
    submitted = qtc.pyqtSignal(int, int, int)

class ViewCrossingForm(qtw.QWidget):

    def __init__(self, model):
        super().__init__()
        #TODO        
        #self._model = model
        #self._controller = controller
        self.initializeUI()
        self.connect_and_emit_trigger()

    def connect_and_emit_trigger(self):
        #connecting a signal to python callables
        # COLLISION HISTORY (5 YEAR PERIOD)
        #collision_history_total_5_year_period - connect signals and slots
        '''
        Connect input variable signals to collision_history_total_5_year_period method slot.
        Required input variables: 
            spinBox_collision_history_fatal_injury, spinBox_collision_history_personal_injury, spinBox_collision_history_property_damage
        Related methods:
            None
        '''
        self.spinBox_collision_history_fatal_injury.valueChanged.connect(lambda val: self.handle_collision_history_total_5_year_period('spinBox_collision_history_fatal_injury', val))
        self.spinBox_collision_history_personal_injury.valueChanged.connect(lambda val: self.handle_collision_history_total_5_year_period('spinBox_collision_history_personal_injury', val))
        self.spinBox_collision_history_property_damage.valueChanged.connect(lambda val: self.handle_collision_history_total_5_year_period('spinBox_collision_history_property_damage', val))
        
        #collision_history_risk_index_initial - connect signals and slots
        '''
        Connect input variable signals to collision_history_risk_index_initial method slot.
        Required input variables: 
            spinBox_general_info_road_aadt_current
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_rail_no_tracks_main
            spinBox_general_info_rail_no_tracks_other
            spinBox_general_info_rail_no_trains_per_day_freight
            spinBox_general_info_rail_no_trains_per_day_passengers
            comboBox_inspection_details_gcws_type
            comboBox_general_info_road_classification
            comboBox_grade_crossing_surface_observe_road_approach_surface_type
            comboBox_gcws_observe_gates_n_or_e_approach
            comboBox_gcws_observe_gates_s_or_w_approach
        
        Related methods:
            handle_general_info_rail_railway_design_speed
            handle_general_info_rail_no_tracks_total
            handle_general_info_rail_no_trains_per_day_total
            handle_general_info_road_no_traffic_lanes_total
        '''
        self.spinBox_general_info_road_aadt_current.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_initial('spinBox_general_info_road_aadt_current', val))
        self.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_initial('spinBox_general_info_rail_max_railway_operating_speed_freight', val))
        self.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_initial('spinBox_general_info_rail_max_railway_operating_speed_passenger', val))
        self.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_initial('spinBox_general_info_rail_no_tracks_main', val))
        self.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_initial('spinBox_general_info_rail_no_tracks_other', val))
        self.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_initial('spinBox_general_info_rail_no_trains_per_day_freight', val))
        self.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_initial('spinBox_general_info_rail_no_trains_per_day_passengers', val))
        self.spinBox_general_info_road_no_traffic_lanes_bidirectional.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_initial('spinBox_general_info_road_no_traffic_lanes_bidirectional', val))
        self.spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_initial('spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound', val))
        self.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_initial('spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound', val))
        self.comboBox_inspection_details_gcws_type.currentTextChanged.connect(lambda val: self.handle_collision_history_risk_index_initial('comboBox_inspection_details_gcws_type', val))
        self.comboBox_general_info_road_classification.currentTextChanged.connect(lambda val: self.handle_collision_history_risk_index_initial('comboBox_general_info_road_classification', val))
        self.comboBox_grade_crossing_surface_observe_road_approach_surface_type.currentTextChanged.connect(lambda val: self.handle_collision_history_risk_index_initial('comboBox_grade_crossing_surface_observe_road_approach_surface_type', val))
        self.comboBox_gcws_observe_gates_n_or_e_approach.currentTextChanged.connect(lambda val: self.handle_collision_history_risk_index_initial('comboBox_gcws_observe_gates_n_or_e_approach', val))
        self.comboBox_gcws_observe_gates_s_or_w_approach.currentTextChanged.connect(lambda val: self.handle_collision_history_risk_index_initial('comboBox_gcws_observe_gates_s_or_w_approach', val))
        
        #collision_history_risk_index_final - connect signals and slots
        '''
        Connect input variable signals to collision_history_risk_index_final method slot.
        Required input variables: 
            spinBox_general_info_road_aadt_current
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_rail_no_tracks_main
            spinBox_general_info_rail_no_tracks_other
            spinBox_general_info_rail_no_trains_per_day_freight
            spinBox_general_info_rail_no_trains_per_day_passengers
            comboBox_inspection_details_gcws_type
            comboBox_general_info_road_classification
            comboBox_grade_crossing_surface_observe_road_approach_surface_type
            comboBox_gcws_observe_gates_n_or_e_approach
            comboBox_gcws_observe_gates_s_or_w_approach
            spinBox_collision_history_fatal_injury, 
            spinBox_collision_history_personal_injury, 
            spinBox_collision_history_property_damage
        
        Related methods:
            handle_general_info_rail_railway_design_speed
            handle_general_info_rail_no_tracks_total
            handle_general_info_rail_no_trains_per_day_total
            handle_general_info_road_no_traffic_lanes_total
            handle_collision_history_total_5_year_period
        '''
        self.spinBox_general_info_road_aadt_current.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_final('spinBox_general_info_road_aadt_current', val))
        self.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_final('spinBox_general_info_rail_max_railway_operating_speed_freight', val))
        self.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_final('spinBox_general_info_rail_max_railway_operating_speed_passenger', val))
        self.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_final('spinBox_general_info_rail_no_tracks_main', val))
        self.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_final('spinBox_general_info_rail_no_tracks_other', val))
        self.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_final('spinBox_general_info_rail_no_trains_per_day_freight', val))
        self.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_final('spinBox_general_info_rail_no_trains_per_day_passengers', val))
        self.spinBox_general_info_road_no_traffic_lanes_bidirectional.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_final('spinBox_general_info_road_no_traffic_lanes_bidirectional', val))
        self.spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_final('spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound', val))
        self.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_final('spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound', val))
        self.comboBox_inspection_details_gcws_type.currentTextChanged.connect(lambda val: self.handle_collision_history_risk_index_final('comboBox_inspection_details_gcws_type', val))
        self.comboBox_general_info_road_classification.currentTextChanged.connect(lambda val: self.handle_collision_history_risk_index_final('comboBox_general_info_road_classification', val))
        self.comboBox_grade_crossing_surface_observe_road_approach_surface_type.currentTextChanged.connect(lambda val: self.handle_collision_history_risk_index_final('comboBox_grade_crossing_surface_observe_road_approach_surface_type', val))
        self.comboBox_gcws_observe_gates_n_or_e_approach.currentTextChanged.connect(lambda val: self.handle_collision_history_risk_index_final('comboBox_gcws_observe_gates_n_or_e_approach', val))
        self.comboBox_gcws_observe_gates_s_or_w_approach.currentTextChanged.connect(lambda val: self.handle_collision_history_risk_index_final('comboBox_gcws_observe_gates_s_or_w_approach', val))
        self.spinBox_collision_history_fatal_injury.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_final('spinBox_collision_history_fatal_injury', val))
        self.spinBox_collision_history_personal_injury.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_final('spinBox_collision_history_personal_injury', val))
        self.spinBox_collision_history_property_damage.valueChanged.connect(lambda val: self.handle_collision_history_risk_index_final('spinBox_collision_history_property_damage', val))

        # GENERAL INFORMATION
        #general_info_rail_no_tracks_total - connect signals and slots
        '''
        Connect input variable signals to general_info_rail_no_tracks_total method slot.
        Required input variables: 
            spinBox_general_info_rail_no_tracks_main, spinBox_general_info_rail_no_tracks_other
        Related methods:
            None
        '''
        self.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(lambda val: self.handle_general_info_rail_no_tracks_total('spinBox_general_info_rail_no_tracks_main', val))
        self.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(lambda val: self.handle_general_info_rail_no_tracks_total('spinBox_general_info_rail_no_tracks_other', val))
        
        #general_info_rail_no_trains_per_day_total - connect signals and slots
        '''
        Connect input variable signals to general_info_rail_no_trains_per_day_total method slot.
        Required input variables: 
            spinBox_general_info_rail_no_trains_per_day_freight, spinBox_general_info_rail_no_trains_per_day_passengers
        Related methods:
            None
        '''
        self.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(lambda val: self.handle_general_info_rail_no_trains_per_day_total('spinBox_general_info_rail_no_trains_per_day_freight', val))
        self.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(lambda val: self.handle_general_info_rail_no_trains_per_day_total('spinBox_general_info_rail_no_trains_per_day_passengers', val))
        
        #general_info_road_no_traffic_lanes_total - connect signals and slots
        '''
        Connect input variable signals to general_info_road_no_traffic_lanes_total method slot.
        Required input variables: 
            spinBox_general_info_road_no_traffic_lanes_bidirectional, spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound, spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound
        Related methods:
            None
        '''
        self.spinBox_general_info_road_no_traffic_lanes_bidirectional.valueChanged.connect(lambda val: self.handle_general_info_road_no_traffic_lanes_total('spinBox_general_info_road_no_traffic_lanes_bidirectional', val))
        self.spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound.valueChanged.connect(lambda val: self.handle_general_info_road_no_traffic_lanes_total('spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound', val))
        self.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound.valueChanged.connect(lambda val: self.handle_general_info_road_no_traffic_lanes_total('spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound', val))
        
        #general_info_rail_railway_design_speed - connect signals and slots
        '''
        Connect input variable signals to general_info_rail_railway_design_speed method slot.
        Required input variables: 
            spinBox_general_info_rail_max_railway_operating_speed_freight, spinBox_general_info_rail_max_railway_operating_speed_passenger
        Related methods:
            None
        '''
        self.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(lambda val: self.handle_general_info_rail_railway_design_speed('spinBox_general_info_rail_max_railway_operating_speed_freight', val))
        self.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(lambda val: self.handle_general_info_rail_railway_design_speed('spinBox_general_info_rail_max_railway_operating_speed_passenger', val))        
        
        # DESIGN CONSIDERATIONS (GCS SECTION 10)
        #design_calculate_adjacent_track_clearance_time - connect signals and slots
        '''
        Connect input variable signals to design_calculate_adjacent_track_clearance_time method slot.
        Required input variables: 
            doubleSpinBox_design_measure_adjacent_track_separation_distance, doubleSpinBox_design_measure_adjacent_track_clearance_distance
        Related methods:
            None
        '''
        self.doubleSpinBox_design_measure_adjacent_track_separation_distance.valueChanged.connect(lambda val: self.handle_design_calculate_adjacent_track_clearance_time('doubleSpinBox_design_measure_adjacent_track_separation_distance', val))
        self.doubleSpinBox_design_measure_adjacent_track_clearance_distance.valueChanged.connect(lambda val: self.handle_design_calculate_adjacent_track_clearance_time('doubleSpinBox_design_measure_adjacent_track_clearance_distance', val))

        #design_calculate_clearance_time_crossing_pedestrian_design_check - connect signals and slots
        '''
        Connect input variable signals to design_calculate_clearance_time_crossing_pedestrian_design_check method slot.
        Required input variables: 
            doubleSpinBox_design_measure_clearance_distance_pedestrian
        Related methods:
            None
        '''
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(lambda val: self.handle_design_calculate_clearance_time_pedestrian_design_check('doubleSpinBox_design_measure_clearance_distance_pedestrian', val))

        #design_calculate_clearance_time_vehicle_design_check - connect signals and slots 
        '''
        Connect input variable signals to design_calculate_clearance_time_vehicle_design_check method slot.
        Required input variables: 
            doubleSpinBox_design_measure_clearance_distance_pedestrian
            doubleSpinBox_design_measure_clearance_distance_vehicle
            doubleSpinBox_design_road_max_approach_grade_within_s
            combo_Box_design_road_design_vehicle_type        
        Related methods:
            handle_design_input_reaction_time
            handle_design_calculate_vehicle_departure_time_grade_adjusted
            handle_design_calculate_vehicle_departure_time
            handle_design_calculate_vehicle_travel_distance
            handle_design_lookup_design_vehicle_length
            handle_design_lookup_design_vehicle_class
            handle_design_lookup_grade_adjustment_factor
        '''
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(lambda val: self.handle_design_calculate_clearance_time_vehicle_design_check('doubleSpinBox_design_measure_clearance_distance_pedestrian', val))
        self.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(lambda val: self.handle_design_calculate_clearance_time_vehicle_design_check('doubleSpinBox_design_measure_clearance_distance_vehicle', val))
        self.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(lambda val: self.handle_design_calculate_clearance_time_vehicle_design_check('doubleSpinBox_design_road_max_approach_grade_within_s', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_design_calculate_clearance_time_vehicle_design_check('comboBox_design_road_design_vehicle_type', val))                                                                     

        #TODO 
        #self.label_design_measure_clearance_distance_gate_arm_ssd = qtw.QLabel('No Value')

        #design_calculate_gate_arm_clearance_time_vehicle_ssd - connect signals and slots
        '''
        Connect input variable signals to design_calculate_gate_arm_clearance_time_vehicle_ssd method slot.
        Required input variables: 
            spinBox_general_info_road_speed_design
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            comboBox_design_road_design_vehicle_type     
        Related methods:
            handle_design_lookup_design_vehicle_length
            handle_sightlines_lookup_ssd_minimum_n_or_e_approach
            handle_sightlines_lookup_ssd_minimum_s_or_w_approach
        '''
        self.spinBox_general_info_road_speed_design.valueChanged.connect(lambda val: self.handle_design_calculate_gate_arm_clearance_time_vehicle_ssd('spinBox_general_info_road_speed_design', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(lambda val: self.handle_design_calculate_gate_arm_clearance_time_vehicle_ssd('doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(lambda val: self.handle_design_calculate_gate_arm_clearance_time_vehicle_ssd('doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_design_calculate_gate_arm_clearance_time_vehicle_ssd('comboBox_design_road_design_vehicle_type', val))

        #design_calculate_gate_arm_clearance_time_vehicle_stop - connect signals and slots
        '''
        Connect input variable signals to design_calculate_gate_arm_clearance_time_vehicle_stop method slot.
        Required input variables:
            doubleSpinBox_design_measure_clearance_distance_pedestrian 
            doubleSpinBox_design_road_max_approach_grade_within_s
            comboBox_design_road_design_vehicle_type
        Related methods:
            label_design_input_reaction_time
            handle_design_calculate_vehicle_departure_time_gate_arm_clearance
            handle_design_lookup_grade_adjustment_factor
            handle_design_lookup_design_vehicle_class
            handle_design_lookup_design_vehicle_length
        '''
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(lambda val: self.handle_design_calculate_gate_arm_clearance_time_vehicle_stop('doubleSpinBox_design_measure_clearance_distance_pedestrian', val))
        self.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(lambda val: self.handle_design_calculate_gate_arm_clearance_time_vehicle_stop('doubleSpinBox_design_road_max_approach_grade_within_s', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_design_calculate_gate_arm_clearance_time_vehicle_stop('comboBox_design_road_design_vehicle_type', val))

        #design_calculate_gate_arm_clearance_time_vehicle_recommended - connect signals and slots
        '''
        Connect input variable signals to design_calculate_gate_arm_clearance_time_vehicle_recommended method slot.
        Required input variables: 
            spinBox_general_info_road_speed_design
            doubleSpinBox_design_measure_clearance_distance_pedestrian
            doubleSpinBox_design_road_max_approach_grade_within_s
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach
            comboBox_design_road_design_vehicle_type
        Related methods:
            label_design_input_reaction_time
            handle_design_calculate_gate_arm_clearance_time_vehicle_ssd
            handle_design_calculate_gate_arm_clearance_time_vehicle_stop
            handle_design_calculate_vehicle_departure_time_gate_arm_clearance
            handle_design_lookup_design_vehicle_class
            handle_design_lookup_design_vehicle_length
            handle_design_lookup_grade_adjustment_factor
            handle_sightlines_lookup_ssd_minimum_n_or_e_approach
            handle_sightlines_lookup_ssd_minimum_s_or_w_approach
        '''
        self.spinBox_general_info_road_speed_design.valueChanged.connect(lambda val: self.handle_design_calculate_gate_arm_clearance_time_vehicle_recommended('spinBox_general_info_road_speed_design', val))
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(lambda val: self.handle_design_calculate_gate_arm_clearance_time_vehicle_recommended('doubleSpinBox_design_measure_clearance_distance_pedestrian', val))
        self.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(lambda val: self.handle_design_calculate_gate_arm_clearance_time_vehicle_recommended('doubleSpinBox_design_road_max_approach_grade_within_s', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(lambda val: self.handle_design_calculate_gate_arm_clearance_time_vehicle_recommended('doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(lambda val: self.handle_design_calculate_gate_arm_clearance_time_vehicle_recommended('doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_design_calculate_gate_arm_clearance_time_vehicle_recommended('comboBox_design_road_design_vehicle_type', val))

        #design_calculate_vehicle_travel_distance - connect signals and slots
        '''
        Connect input variable signals to design_calculate_vehicle_travel_distance method slot.
        Required input variables:
            doubleSpinBox_design_measure_clearance_distance_vehicle
            comboBox_design_road_design_vehicle_type
        Related methods:
            handle_design_lookup_design_vehicle_length 
        ''' 
        self.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(lambda val: self.handle_design_calculate_vehicle_travel_distance('doubleSpinBox_design_measure_clearance_distance_vehicle', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_design_calculate_vehicle_travel_distance('comboBox_design_road_design_vehicle_type', val))
        
        #design_calculate_vehicle_departure_time - connect signals and slots
        '''
        Connect input variable signals to design_calculate_vehicle_departure_time method slot.
        Required input variables:
            doubleSpinBox_design_measure_clearance_distance_pedestrian
            doubleSpinBox_design_measure_clearance_distance_vehicle
            comboBox_design_road_design_vehicle_type
        Related methods:
            handle_design_calculate_vehicle_travel_distance
            handle_design_lookup_design_vehicle_class
            handle_design_lookup_design_vehicle_length
        ''' 
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(lambda val: self.handle_design_calculate_vehicle_departure_time('doubleSpinBox_design_measure_clearance_distance_pedestrian', val))
        self.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(lambda val: self.handle_design_calculate_vehicle_departure_time('doubleSpinBox_design_measure_clearance_distance_vehicle', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_design_calculate_vehicle_departure_time('comboBox_design_road_design_vehicle_type', val))

        #design_calculate_vehicle_departure_time_grade_adjusted - connect signals and slots
        '''
        Connect input variable signals to design_calculate_vehicle_departure_time_grade_adjusted method slot.
        Required input variables:
           doubleSpinBox_design_measure_clearance_distance_pedestrian
           doubleSpinBox_design_measure_clearance_distance_vehicle
           doubleSpinBox_design_road_max_approach_grade_within_s
           comboBox_design_road_design_vehicle_type
        Related methods:
            handle_design_calculate_vehicle_departure_time
            handle_design_calculate_vehicle_travel_distance
            handle_design_lookup_design_vehicle_class
            handle_design_lookup_design_vehicle_length
            handle_design_lookup_grade_adjustment_factor
        '''
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(lambda val: self.handle_design_calculate_vehicle_departure_time_grade_adjusted('doubleSpinBox_design_measure_clearance_distance_pedestrian', val))
        self.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(lambda val: self.handle_design_calculate_vehicle_departure_time_grade_adjusted('doubleSpinBox_design_measure_clearance_distance_vehicle', val))
        self.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(lambda val:self.handle_design_calculate_vehicle_departure_time_grade_adjusted('doubleSpinBox_design_road_max_approach_grade_within_s', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_design_calculate_vehicle_departure_time_grade_adjusted('comboBox_design_road_design_vehicle_type', val))

        #design_calculate_vehicle_departure_time_gate_arm_clearance - connect signals and slots
        '''
        Connect input variable signals to design_calculate_vehicle_departure_time_gate_arm_clearance method slot.
        Required input variables:
            comboBox_design_road_design_vehicle_type
        Related methods:    
            handle_design_lookup_design_vehicle_class
            handle_design_lookup_design_vehicle_length
        '''
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_design_calculate_vehicle_departure_time_gate_arm_clearance('comboBox_design_road_design_vehicle_type', val))
        
        #TODO
        #design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted - connect signals and slots
        '''
        Connect input variable signals to design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted method slot.
        Required input variables:
            doubleSpinBox_design_road_max_approach_grade_within_s
            comboBox_design_road_design_vehicle_type
        Related methods:    
            handle_design_calculate_vehicle_departure_time_gate_arm_clearance
            handle_design_lookup_design_vehicle_class
            handle_design_lookup_design_vehicle_length
            handle_design_lookup_grade_adjustment_factor
        ''' 
        self.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(lambda val: self.handle_design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted('doubleSpinBox_design_road_max_approach_grade_within_s', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted('comboBox_design_road_design_vehicle_type', val))

        #design_lookup_design_vehicle_class - connect signals and slots
        '''
        Connect input variable signals to design_lookup_design_vehicle_class method slot.
        Required input variables: 
            comboBox_design_road_design_vehicle_type
        Related methods:
            None
        ''' 
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_design_lookup_design_vehicle_class('comboBox_design_road_design_vehicle_type', val))

        #design_lookup_design_vehicle_length - connect signals and slots
        '''
        Connect input variable signals to design_lookup_design_vehicle_length method slot.
        Required input variables: 
            comboBox_design_road_design_vehicle_type
        Related methods:
            None
        ''' 
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_design_lookup_design_vehicle_length('comboBox_design_road_design_vehicle_type', val))
                
        #design_lookup_grade_adjustment_factor - connect signals and slots
        '''
        Connect input variable signals to design_lookup_grade_adjustment_factor method slot.
        Required input variables:
            doubleSpinBox_design_road_max_approach_grade_within_s
            comboBox_design_road_design_vehicle_type
        Related methods:
            None
        ''' 
        self.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(lambda val: self.handle_design_lookup_grade_adjustment_factor('doubleSpinBox_design_road_max_approach_grade_within_s', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_design_lookup_grade_adjustment_factor('comboBox_design_road_design_vehicle_type', val))

        #TODO
        #design_measure_clearance_distance_gate_arm_stop - connect signals and slots

        # ROAD GEOMETRY (GCS SECTION 6)
        #road_geometry_lookup_gradient_difference - connect signals and slots
        '''
        Connect input variable signals to road_geometry_lookup_gradient_difference method slot.
        Required input variables:
            comboBox_general_info_road_classification
        Related methods:
            None
        ''' 
        self.comboBox_general_info_road_classification.currentTextChanged.connect(lambda val: self.handle_road_geometry_lookup_gradient_difference('comboBox_general_info_road_classification', val))
        
        # SIGHTLINES (GCS SECTION 7)
        #sightlines_lookup_existing_active_crossing - connect signals and slots
        '''
        Connect input variable signals to sightlines_lookup_existing_active_crossing method slot.
        Required input variables:
            comboBox_inspection_details_gcws_type
        Related methods:
            None
        ''' 
        self.comboBox_inspection_details_gcws_type.currentTextChanged.connect(lambda val: self.handle_sightlines_lookup_existing_active_crossing('comboBox_inspection_details_gcws_type', val))
        
        #sightlines_lookup_existing_active_crossing_with_gates - connect signals and slots
        '''
        Connect input variable signals to sightlines_lookup_existing_active_crossing_with_gates method slot.
        Required input variables:
            comboBox_inspection_details_gcws_type
            comboBox_gcws_observe_gates_n_or_e_approach
            comboBox_gcws_observe_gates_s_or_w_approach
        Related methods:
            None
        '''
        self.comboBox_inspection_details_gcws_type.currentTextChanged.connect(lambda val: self.handle_sightlines_lookup_existing_active_crossing_with_gates('comboBox_inspection_details_gcws_type', val))
        self.comboBox_gcws_observe_gates_n_or_e_approach.currentTextChanged.connect(lambda val: self.handle_sightlines_lookup_existing_active_crossing_with_gates('comboBox_gcws_observe_gates_n_or_e_approach', val))
        self.comboBox_gcws_observe_gates_s_or_w_approach.currentTextChanged.connect(lambda val: self.handle_sightlines_lookup_existing_active_crossing_with_gates('comboBox_gcws_observe_gates_s_or_w_approach', val))

        #sightlines_calculate_dstopped_pedestrian_min_ft - connect signals and slots
        '''
        Connect input variable signals to sightlines_calculate_dstopped_pedestrian_min_ft method slot.
        Required input variables:
            doubleSpinBox_design_measure_clearance_distance_pedestrian
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
        Related methods: 
            handle_design_calculate_clearance_time_pedestrian_design_check       
            handle_general_info_rail_railway_design_speed
        '''
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dstopped_pedestrian_min_ft('doubleSpinBox_design_measure_clearance_distance_pedestrian', val))
        self.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dstopped_pedestrian_min_ft('spinBox_general_info_rail_max_railway_operating_speed_freight', val))
        self.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dstopped_pedestrian_min_ft('spinBox_general_info_rail_max_railway_operating_speed_passenger', val))

        #sightlines_calculate_dstopped_pedestrian_min_m - connect signals and slots
        '''
        Connect input variable signals to sightlines_calculate_dstopped_pedestrian_min_m method slot.
        Required input variables:
            doubleSpinBox_design_measure_clearance_distance_pedestrian
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
        Related methods: 
            handle_design_calculate_clearance_time_pedestrian_design_check       
            handle_general_info_rail_railway_design_speed
        '''
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dstopped_pedestrian_min_m('doubleSpinBox_design_measure_clearance_distance_pedestrian', val))
        self.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dstopped_pedestrian_min_m('spinBox_general_info_rail_max_railway_operating_speed_freight', val))
        self.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dstopped_pedestrian_min_m('spinBox_general_info_rail_max_railway_operating_speed_passenger', val))

        #TODO contains pedestrian clearance distance
        #sightlines_calculate_dstopped_vehicle_min_ft - connect signals and slots
        '''
        Connect input variable signals to sightlines_calculate_dstopped_vehicle_min_ft method slot.
        Required input variables:
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            doubleSpinBox_design_measure_clearance_distance_pedestrian
            doubleSpinBox_design_measure_clearance_distance_vehicle
            doubleSpinBox_design_road_max_approach_grade_within_s
            comboBox_design_road_design_vehicle_type
        Related methods: 
            label_design_input_reaction_time
            handle_general_info_rail_railway_design_speed
            handle_design_calculate_clearance_time_vehicle_design_check
            handle_design_calculate_vehicle_departure_time_grade_adjusted
            handle_design_calculate_vehicle_departure_time
            handle_design_lookup_design_vehicle_class
            handle_design_calculate_vehicle_travel_distance
            handle_design_lookup_grade_adjustment_factor
        '''
        self.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dstopped_vehicle_min_ft('spinBox_general_info_rail_max_railway_operating_speed_freight', val))
        self.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dstopped_vehicle_min_ft('spinBox_general_info_rail_max_railway_operating_speed_passenger', val))
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dstopped_vehicle_min_ft('doubleSpinBox_design_measure_clearance_distance_pedestrian', val))
        self.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dstopped_vehicle_min_ft('doubleSpinBox_design_measure_clearance_distance_vehicle', val))
        self.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dstopped_vehicle_min_ft('doubleSpinBox_design_road_max_approach_grade_within_s', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_sightlines_calculate_dstopped_vehicle_min_ft('comboBox_design_road_design_vehicle_type', val))

        #sightlines_calculate_dstopped_vehicle_min_m - connect signals and slots
        '''
        Connect input variable signals to sightlines_calculate_dstopped_vehicle_min_m method slot.
        Required input variables:
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            doubleSpinBox_design_measure_clearance_distance_pedestrian
            doubleSpinBox_design_measure_clearance_distance_vehicle
            doubleSpinBox_design_road_max_approach_grade_within_s
            comboBox_design_road_design_vehicle_type
        Related methods: 
            label_design_input_reaction_time
            handle_general_info_rail_railway_design_speed
            handle_design_calculate_clearance_time_vehicle_design_check
            handle_design_calculate_vehicle_departure_time_grade_adjusted
            handle_design_calculate_vehicle_departure_time
            handle_design_lookup_design_vehicle_class
            handle_design_calculate_vehicle_travel_distance
            handle_design_lookup_grade_adjustment_factor
        '''
        self.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dstopped_vehicle_min_m('spinBox_general_info_rail_max_railway_operating_speed_freight', val))
        self.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dstopped_vehicle_min_m('spinBox_general_info_rail_max_railway_operating_speed_passenger', val))
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dstopped_vehicle_min_m('doubleSpinBox_design_measure_clearance_distance_pedestrian', val))
        self.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dstopped_vehicle_min_m('doubleSpinBox_design_measure_clearance_distance_vehicle', val))
        self.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dstopped_vehicle_min_m('doubleSpinBox_design_road_max_approach_grade_within_s', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_sightlines_calculate_dstopped_vehicle_min_m('comboBox_design_road_design_vehicle_type', val))

        #sightlines_lookup_ssd_minimum_n_or_e_approach - connect signals and slots
        '''
        Connect input variable signals to sightlines_lookup_ssd_minimum_n_or_e_approach method slot.
        Required input variables:
            spinBox_general_info_road_speed_design
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            comboBox_design_road_design_vehicle_type
        Related methods: 
            handle_design_lookup_design_vehicle_class
        '''
        self.spinBox_general_info_road_speed_design.valueChanged.connect(lambda val: self.handle_sightlines_lookup_ssd_minimum_n_or_e_approach('spinBox_general_info_road_speed_design', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(lambda val: self.handle_sightlines_lookup_ssd_minimum_n_or_e_approach('doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_sightlines_lookup_ssd_minimum_n_or_e_approach('comboBox_design_road_design_vehicle_type', val))

        #sightlines_lookup_ssd_minimum_s_or_w_approach - connect signals and slots
        '''
        Connect input variable signals to sightlines_lookup_ssd_minimum_s_or_w_approach method slot.
        Required input variables:
            spinBox_general_info_road_speed_design
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach
            comboBox_design_road_design_vehicle_type
        Related methods: 
            handle_design_lookup_design_vehicle_class
        '''
        self.spinBox_general_info_road_speed_design.valueChanged.connect(lambda val: self.handle_sightlines_lookup_ssd_minimum_s_or_w_approach('spinBox_general_info_road_speed_design', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(lambda val: self.handle_sightlines_lookup_ssd_minimum_s_or_w_approach('doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_sightlines_lookup_ssd_minimum_s_or_w_approach('comboBox_design_road_design_vehicle_type', val))

        #sightlines_calculate_dssd_vehicle_min_ft - connect signals and slots
        '''
        Connect input variable signals to sightlines_calculate_dssd_vehicle_min_ft method slot.
        Required input variables:
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_road_speed_design
            doubleSpinBox_design_measure_clearance_distance_vehicle
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach
            comboBox_design_road_design_vehicle_type 
        Related methods: 
            handle_design_lookup_design_vehicle_class
            handle_design_lookup_design_vehicle_length
            handle_general_info_rail_railway_design_speed
            handle_sightlines_lookup_ssd_minimum_n_or_e_approach
            handle_sightlines_lookup_ssd_minimum_s_or_w_approach
        '''
        self.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dssd_vehicle_min_ft('spinBox_general_info_rail_max_railway_operating_speed_freight', val))
        self.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dssd_vehicle_min_ft('spinBox_general_info_rail_max_railway_operating_speed_passenger', val))
        self.spinBox_general_info_road_speed_design.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dssd_vehicle_min_ft('spinBox_general_info_road_speed_design', val))
        self.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dssd_vehicle_min_ft('doubleSpinBox_design_measure_clearance_distance_vehicle', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dssd_vehicle_min_ft('doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dssd_vehicle_min_ft('doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_sightlines_calculate_dssd_vehicle_min_ft('comboBox_design_road_design_vehicle_type', val))
        
        #sightlines_calculate_dssd_vehicle_min_m - connect signals and slots
        '''
        Connect input variable signals to sightlines_calculate_dssd_vehicle_min_m method slot.
        Required input variables:
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_road_speed_design
            doubleSpinBox_design_measure_clearance_distance_vehicle
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach
            comboBox_design_road_design_vehicle_type 
        Related methods: 
            handle_design_lookup_design_vehicle_class
            handle_design_lookup_design_vehicle_length
            handle_general_info_rail_railway_design_speed
            handle_sightlines_lookup_ssd_minimum_n_or_e_approach
            handle_sightlines_lookup_ssd_minimum_s_or_w_approach
        '''
        self.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dssd_vehicle_min_m('spinBox_general_info_rail_max_railway_operating_speed_freight', val))
        self.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dssd_vehicle_min_m('spinBox_general_info_rail_max_railway_operating_speed_passenger', val))
        self.spinBox_general_info_road_speed_design.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dssd_vehicle_min_m('spinBox_general_info_road_speed_design', val))
        self.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dssd_vehicle_min_m('doubleSpinBox_design_measure_clearance_distance_vehicle', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dssd_vehicle_min_m('doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(lambda val: self.handle_sightlines_calculate_dssd_vehicle_min_m('doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_sightlines_calculate_dssd_vehicle_min_m('comboBox_design_road_design_vehicle_type', val))

        # GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
        #TODO
        #gcws_warrant_private_9_3 - connect signals and slots
        # .valueChanged.connect(self.handle_gcws_warrant_private_9_3)

        #TODO
        #gcws_warrant_private_9_3_1 - connect signals and slots
        # .valueChanged.connect(self.handle_gcws_warrant_private_9_3_1)
        
        #TODO
        #gcws_warrant_private_9_3_2_a - connect signals and slots
        # .valueChanged.connect(self.handle_gcws_warrant_private_9_3_2_a)
        
        #TODO
        #gcws_warrant_private_9_3_2_b - connect signals and slots
        # .valueChanged.connect(self.handle_gcws_warrant_private_9_3_2_b)
        
        #TODO
        #gcws_warrant_private_9_3_2_c - connect signals and slots
        # .valueChanged.connect(self.handle_gcws_warrant_private_9_3_2_c)

        #TODO
        #gcws_warrant_public_9_1 - connect signals and slots
        # .valueChanged.connect(self.handle_gcws_warrant_public_9_1)

        #TODO
        #gcws_warrant_public_9_1_a - connect signals and slots
        # .valueChanged.connect(self.handle_gcws_warrant_public_9_1_a)

        #TODO
        #gcws_warrant_public_9_1_b - connect signals and slots
        # .valueChanged.connect(self.handle_gcws_warrant_public_9_1_b)

        #TODO
        #gcws_warrant_public_9_1_c - connect signals and slots
        # .valueChanged.connect(self.handle_gcws_warrant_public_9_1_c)

        #TODO
        #gcws_warrant_public_9_1_d_i - connect signals and slots
        # .valueChanged.connect(self.handle_gcws_warrant_public_9_1_d_i)

        #TODO
        #gcws_warrant_public_9_1_d_ii - connect signals and slots
        # .valueChanged.connect(self.handle_gcws_warrant_public_9_1_d_ii)
        
        #TODO
        #gcws_warrant_public_9_1_d_iii - connect signals and slots
        # .valueChanged.connect(self.handle_gcws_warrant_public_9_1_d_iii)

        #TODO
        #gcws_warrant_sidewalk_9_5 - connect signals and slots
        # .valueChanged.connect(self.handle_gcws_warrant_sidewalk_9_5)

        #TODO
        #gates_gcws_warrant_private_9_4_1_a - connect signals and slots
        # .valueChanged.connect(self.handle_gates_gcws_warrant_private_9_4_1_a)

        #TODO
        #gates_gcws_warrant_private_9_4_1_b - connect signals and slots
        # .valueChanged.connect(self.handle_gates_gcws_warrant_private_9_4_1_b)

        #TODO
        #gates_gcws_warrant_private_9_4_1_c - connect signals and slots
        # .valueChanged.connect(self.handle_gates_gcws_warrant_private_9_4_1_c)

        #TODO
        #gates_gcws_warrant_public_9_2_1_a - connect signals and slots
        # .valueChanged.connect(self.handle_gates_gcws_warrant_public_9_2_1_a)

        #TODO
        #gates_gcws_warrant_public_9_2_1_b - connect signals and slots
        # .valueChanged.connect(self.handle_gates_gcws_warrant_public_9_2_1_b)

        #TODO
        #gates_gcws_warrant_public_9_2_1_c - connect signals and slots
        # .valueChanged.connect(self.handle_gates_gcws_warrant_public_9_2_1_c)

        #TODO
        #gates_gcws_warrant_public_9_2_1_d - connect signals and slots
        # .valueChanged.connect(self.handle_gates_gcws_warrant_public_9_2_1_d)

        #TODO
        #gates_gcws_warrant_public_9_2_1_e - connect signals and slots
        # .valueChanged.connect(self.handle_gates_gcws_warrant_public_9_2_1_e)

        #TODO
        #gates_gcws_warrant_sidewalk_9_6 - connect signals and slots
        # .valueChanged.connect(self.handle_gates_gcws_warrant_sidewalk_9_6)

        #GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
        #TODO
        #gcws_rail_design_warning_time_adjacent_crossing - connect signals and slots
        # .valueChanged.connect(self.handle_gcws_rail_design_warning_time_adjacent_crossing)
        
        #TODO includes pedestrian clearance
        #gcws_rail_design_warning_time_clearance_distance - connect signals and slots
        '''
        Connect input variable signals to gcws_rail_design_warning_time_clearance_distance method slot.
        Required input variables:
            comboBox_design_road_design_vehicle_type
            doubleSpinBox_design_measure_clearance_distance_pedestrian
            doubleSpinBox_design_measure_clearance_distance_vehicle 
        Related methods:
            None
        '''
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_clearance_distance('comboBox_design_road_design_vehicle_type', val))
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_clearance_distance('doubleSpinBox_design_measure_clearance_distance_pedestrian', val))
        self.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_clearance_distance('doubleSpinBox_design_measure_clearance_distance_vehicle', val))
        
        #gcws_rail_design_warning_time_departure_time_vehicle - connect signals and slots
        '''
        Connect input variable signals to gcws_rail_design_warning_time_departure_time_vehicle method slot.
        Required input variables:
            doubleSpinBox_design_measure_clearance_distance_pedestrian
            doubleSpinBox_design_measure_clearance_distance_vehicle
            doubleSpinBox_design_road_max_approach_grade_within_s
            combo_Box_design_road_design_vehicle_type        
        Related methods:
            handle_design_calculate_clearance_time_vehicle_design_check
            handle_design_input_reaction_time
            handle_design_calculate_vehicle_departure_time_grade_adjusted
            handle_design_calculate_vehicle_departure_time
            handle_design_calculate_vehicle_travel_distance
            handle_design_lookup_design_vehicle_length
            handle_design_lookup_design_vehicle_class
            handle_design_lookup_grade_adjustment_factor
        '''
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_departure_time_vehicle('doubleSpinBox_design_measure_clearance_distance_pedestrian', val))
        self.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_departure_time_vehicle('doubleSpinBox_design_measure_clearance_distance_vehicle', val))
        self.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_departure_time_vehicle('doubleSpinBox_design_road_max_approach_grade_within_s', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_departure_time_vehicle('comboBox_design_road_design_vehicle_type', val))

        #gcws_rail_design_warning_time_departure_time_pedestrian - connect signals and slots
        '''
        Connect input variable signals to gcws_rail_design_warning_time_departure_time_pedestrian method slot.
        Required input variables:
            doubleSpinBox_design_measure_clearance_distance_pedestrian
        Related methods:
            handle_design_calculate_clearance_time_pedestrian_design_check
        '''
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_departure_time_pedestrian('doubleSpinBox_design_measure_clearance_distance_pedestrian', val))

        #gcws_rail_design_warning_time_gate_arm_clearance - connect signals and slots
        '''
        Connect input variable signals to gcws_rail_design_warning_time_gate_arm_clearance method slot.
        Required input variables:
            spinBox_general_info_road_speed_design
            doubleSpinBox_design_road_max_approach_grade_within_s
            doubleSpinBox_gates_gcws_rail_gate_arm_descent_time_design
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach
            comboBox_design_road_design_vehicle_type

        Related methods:
            label_design_input_reaction_time
            handle_design_calculate_gate_arm_clearance_time_vehicle_recommended
            handle_design_calculate_gate_arm_clearance_time_vehicle_ssd
            handle_design_lookup_design_vehicle_class
            handle_design_lookup_design_vehicle_length
            handle_sightlines_lookup_ssd_minimum_n_or_e_approach
            handle_sightlines_lookup_ssd_minimum_s_or_w_approach
            handle_design_calculate_gate_arm_clearance_time_vehicle_stop
            handle_design_lookup_grade_adjustment_factor
            handle_design_calculate_vehicle_departure_time_gate_arm_clearance
        '''
        self.spinBox_general_info_road_speed_design.valueChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_gate_arm_clearance('spinBox_general_info_road_speed_design', val))
        #TODO Remove Pedestrian clearance distance
        # self.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_gate_arm_clearance('doubleSpinBox_design_measure_clearance_distance_pedestrian', val))
        self.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_gate_arm_clearance('doubleSpinBox_design_road_max_approach_grade_within_s', val))
        self.doubleSpinBox_gates_gcws_rail_gate_arm_descent_time_design.valueChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_gate_arm_clearance('doubleSpinBox_gates_gcws_rail_gate_arm_descent_time_design', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_gate_arm_clearance('doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_gate_arm_clearance('doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_gate_arm_clearance('comboBox_design_road_design_vehicle_type', val))
        
        #TODO
        #gcws_rail_design_warning_time_preemption - connect signals and slots
        # .valueChanged.connect(self.handle_gcws_rail_design_warning_time_preemption)
        
        #gcws_rail_design_warning_time_ssd - connect signals and slots
        '''
        Connect input variable signals to gcws_rail_design_warning_time_ssd method slot.
        Required input variables:
            spinBox_general_info_road_speed_design
            doubleSpinBox_design_measure_clearance_distance_vehicle
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach
            comboBox_design_road_design_vehicle_type
        Related methods:
            handle_design_calculate_vehicle_travel_distance
            handle_design_lookup_design_vehicle_class
            handle_design_lookup_design_vehicle_length
            handle_sightlines_lookup_ssd_minimum_n_or_e_approach
            handle_sightlines_lookup_ssd_minimum_s_or_w_approach
        '''
        self.spinBox_general_info_road_speed_design.valueChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_ssd('spinBox_general_info_road_speed_design', val))
        self.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_ssd('doubleSpinBox_design_measure_clearance_distance_vehicle', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_ssd('doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_ssd('doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_gcws_rail_design_warning_time_ssd('comboBox_design_road_design_vehicle_type', val))

        #TODO
        #gcws_rail_design_approach_warning_time - connect signals and slots
        # .valueChanged.connect(self.handle_gcws_rail_design_approach_warning_time)
        
        # GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
        
        #TODO
        #gates_gcws_calculate_inner_gate_arm_delay_time_recommended - connect signals and slots
        '''
        Connect input variable signals to gates_gcws_calculate_inner_gate_arm_delay_time_recommended method slot.
        Required input variables: 
            doubleSpinBox_design_measure_adjacent_track_separation_distance, doubleSpinBox_design_measure_adjacent_track_clearance_distance
        Related methods:
            None
        '''
        self.doubleSpinBox_design_measure_adjacent_track_separation_distance.valueChanged.connect(lambda val: self.handle_gates_gcws_calculate_inner_gate_arm_delay_time_recommended('doubleSpinBox_design_measure_adjacent_track_separation_distance', val))
        self.doubleSpinBox_design_measure_adjacent_track_clearance_distance.valueChanged.connect(lambda val: self.handle_gates_gcws_calculate_inner_gate_arm_delay_time_recommended('doubleSpinBox_design_measure_adjacent_track_clearance_distance', val))

        # PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
        #TODO
        #aawd_calculate_advance_activation_time_design_n_or_e_approach - connect signals and slots
        '''
        Connect input variable signals to aawd_calculate_advance_activation_time_design_n_or_e_approach method slot.
        Required input variables:
            spinBox_general_info_road_speed_design
            doubleSpinBox_design_measure_clearance_distance_vehicle
            comboBox_design_road_design_vehicle_type
            spinBox_general_info_road_speed_posted
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach  
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach  
        Related methods:
            handle_design_calculate_vehicle_travel_distance
            handle_design_lookup_design_vehicle_length
            handle_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended
            label_design_input_reaction_time
        '''
        self.spinBox_general_info_road_speed_design.valueChanged.connect(lambda val: self.handle_aawd_calculate_advance_activation_time_design_n_or_e_approach('spinBox_general_info_road_speed_design', val))
        self.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(lambda val: self.handle_aawd_calculate_advance_activation_time_design_n_or_e_approach('doubleSpinBox_design_measure_clearance_distance_vehicle', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(lambda val: self.handle_aawd_calculate_advance_activation_time_design_n_or_e_approach('doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(lambda val: self.handle_aawd_calculate_advance_activation_time_design_n_or_e_approach('doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_aawd_calculate_advance_activation_time_design_n_or_e_approach('comboBox_design_road_design_vehicle_type', val))
        
        #TODO
        #aawd_calculate_advance_activation_time_design_s_or_w_approach - connect signals and slots
        '''
        Connect input variable signals to aawd_calculate_advance_activation_time_design_s_or_w_approach method slot.
        Required input variables:
            spinBox_general_info_road_speed_design
            doubleSpinBox_design_measure_clearance_distance_vehicle
            comboBox_design_road_design_vehicle_type
            spinBox_general_info_road_speed_posted
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach  
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach  
        Related methods:
            handle_design_calculate_vehicle_travel_distance
            handle_design_lookup_design_vehicle_length
            handle_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended
            label_design_input_reaction_time
        '''
        self.spinBox_general_info_road_speed_design.valueChanged.connect(lambda val: self.handle_aawd_calculate_advance_activation_time_design_s_or_w_approach('spinBox_general_info_road_speed_design', val))
        self.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(lambda val: self.handle_aawd_calculate_advance_activation_time_design_s_or_w_approach('doubleSpinBox_design_measure_clearance_distance_vehicle', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(lambda val: self.handle_aawd_calculate_advance_activation_time_design_s_or_w_approach('doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(lambda val: self.handle_aawd_calculate_advance_activation_time_design_s_or_w_approach('doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach', val))
        self.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(lambda val: self.handle_aawd_calculate_advance_activation_time_design_s_or_w_approach('comboBox_design_road_design_vehicle_type', val))

        #TODO
        #aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended - connect signals and slots
        '''
        Connect input variable signals to aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended method slot.
        Required input variables:
            spinBox_general_info_road_speed_posted
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach
        Related methods:
            label_design_input_reaction_time
        '''
        self.spinBox_general_info_road_speed_posted.valueChanged.connect(lambda val: self.handle_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended('spinBox_general_info_road_speed_posted', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(lambda val: self.handle_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended('doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach', val))  
        self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(lambda val: self.handle_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended('doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach', val))  

        #TODO
        #aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended - connect signals and slots
        '''
        Connect input variable signals to aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended method slot.
        Required input variables:
            spinBox_general_info_road_speed_posted
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach
        Related methods:
            label_design_input_reaction_time
        '''
        self.spinBox_general_info_road_speed_posted.valueChanged.connect(lambda val: self.aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended('spinBox_general_info_road_speed_posted', val))
        self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(lambda val: self.aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended('doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach', val))  
        self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(lambda val: self.aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended('doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach', val))

        #TODO
        #aawd_warrant_gcr_lookup_road_classification - connect signals and slots
        '''
        Connect input variable signals to aawd_warrant_gcr_lookup_road_classification method slot.
        Required input variables:
            comboBox_general_info_road_classification
        Related methods:
            None
        '''
        self.comboBox_general_info_road_classification.currentTextChanged.connect(lambda val: self.handle_aawd_warrant_gcr_lookup_road_classification('comboBox_general_info_road_classification', val))

        '''
        #TODO
        #aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr - connect signals and slots
        # .valueChanged.connect(self.handle_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr)
        
        # INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
        #TODO
        #preemption_of_traffic_signals_lookup_proximity_condition - connect signals and slots
        # .valueChanged.connect(self.preemption_of_traffic_signals_lookup_proximity_condition)

        #TODO
        #preemption_of_traffic_signals_lookup_required - connect signals and slots
        # .valueChanged.connect(self.preemption_of_traffic_signals_lookup_required)

        # WHISTLE CESSATION (GCS SECTION Appendix D)
        #TODO
        #areas_without_train_whistling_lookup_gcs_9_2 - connect signals and slots
        # .valueChanged.connect(self.handle_areas_without_train_whistling_lookup_gcs_9_2)
        
        #TODO
        #areas_without_train_whistling_requirements_lookup_table_d1_criteria - connect signals and slots
        
        #TODO
        #areas_without_train_whistling_requirements_observe_table_d1 - connect signals and slots
        # .valueChanged.connect(self.handle_areas_without_train_whistling_requirements_observe_table_D1)
        '''
    
    #Calculate collision_history_total_5_year_period
    def handle_collision_history_total_5_year_period(self, name, value):
        print('handle_collision_history_total_5_year_period', name, value)
        
        collision_history_fatal_injury = self.spinBox_collision_history_fatal_injury.value()
        collision_history_personal_injury = self.spinBox_collision_history_personal_injury.value()
        collision_history_property_damage = self.spinBox_collision_history_property_damage.value()
        
        result = sum([collision_history_fatal_injury, collision_history_personal_injury, collision_history_property_damage])
        self.label_collision_history_total_5_year_period.setNum(result)
        return result
    

    #Calculate collision_history_risk_index_initial
    def handle_collision_history_risk_index_initial(self, name, value):
        print('handle_collision_history_risk_index_initial', name, value)

        general_info_rail_no_tracks_total = self.handle_general_info_rail_no_tracks_total(name, value)
        inspection_details_gcws_type = self.comboBox_inspection_details_gcws_type.currentText()
        gcws_observe_gates_n_or_e_approach = self.comboBox_gcws_observe_gates_n_or_e_approach.currentText()
        gcws_observe_gates_s_or_w_approach = self.comboBox_gcws_observe_gates_s_or_w_approach.currentText()

        grade_crossing_surface_observe_road_approach_surface_type = self.comboBox_grade_crossing_surface_observe_road_approach_surface_type.currentText()
        general_info_road_classification = self.comboBox_general_info_road_classification.currentText()
 
        c = self.spinBox_general_info_road_aadt_current.value()               # c = annual average number of highway vehicles per day (total both directions)
        t = self.handle_general_info_rail_no_trains_per_day_total(name, value) # t = average total train movements per day
        d = self.handle_general_info_rail_no_trains_per_day_total(name, value) # d = average number of thru trains per day during daylight
        mt = self.spinBox_general_info_rail_no_tracks_main.value()             # mt = number of main tracks
        ms = self.handle_general_info_rail_railway_design_speed(name, value)   # ms = maximum timetable speed, mph
        hl = self.handle_general_info_road_no_traffic_lanes_total(name, value) # hl = number of highway lanes
        
        # hp = highway paved, yes = 1.0, no = 2.0
        split_general_info_road_classification = general_info_road_classification.split()

        if not split_general_info_road_classification:
            hp = 'No Value'
        elif split_general_info_road_classification[1] == 'Freeway' and grade_crossing_surface_observe_road_approach_surface_type == 'Asphalt':
            hp = 1.0
        else:
            hp = 2.0

        #ht = highway type factor value
        dict_general_info_road_classification = dict([
            ('Rural Local Undivided', 4),
            ('Rural Collector Undivided', 3),
            ('Rural Collector Divided', 3),
            ('Rural Arterial Undivided', 2),
            ('Rural Arterial Divided', 2),
            ('Rural Freeway Divided', 1),
            ('Urban Local Undivided', 4),
            ('Urban Collector Undivided', 3),
            ('Urban Collector Divided', 3),
            ('Urban Arterial Undivided', 2),
            ('Urban Arterial Divided', 2),
            ('Private Road', 5),
            ('Pedestrian Crossing', 5)
            ])
        if general_info_road_classification == '':
            ht = 'No Value'
        else:
            ht = dict_general_info_road_classification[general_info_road_classification]       

        print('c', c, type(c))
        print('t', t, type(t))
        print('d', d, type(d))
        print('mt', mt, type(mt))
        print('ms', ms, type(ms))
        print('hl', hl, type(hl))
        print('hp', hp, type(hp))
        print('ht', ht, type(ht))

        if inspection_details_gcws_type == '' or general_info_road_classification == '' or grade_crossing_surface_observe_road_approach_surface_type == '' or gcws_observe_gates_n_or_e_approach == '' or gcws_observe_gates_s_or_w_approach == '' or general_info_rail_no_tracks_total == 'No Value' or mt == 'No Value' or c == 0 or t == 'No Value' or d == 'No Value' or ms == 'No Value' or hl == 'No Value' or hp == 'No Value' or ht == 'No Value':            
            result = "No Value"
            self.label_collision_history_risk_index_initial.setText(result)
        elif inspection_details_gcws_type == 'Passive':
            result = round(0.002268 * ((c * t + 0.2)/0.2)**0.3334 * math.exp(0.2094 * mt) * ((d + 0.2)/0.2)**0.1336 * math.exp(-0.616 * (hp - 1)) * math.exp(0.0077 * ms) * math.exp(-0.1000 * (ht - 1)) * 1, 5)
            self.label_collision_history_risk_index_initial.setNum(result)
        elif inspection_details_gcws_type == 'Active' and (gcws_observe_gates_n_or_e_approach != 'Yes' or gcws_observe_gates_s_or_w_approach != 'Yes') and (gcws_observe_gates_n_or_e_approach != '' or gcws_observe_gates_s_or_w_approach != ''):
            result = round(0.003646 * ((c * t + 0.2)/0.2)**0.2953 * math.exp(0.1088 * mt) * ((d + 0.2)/0.2)**0.047 * 1 * 1 * 1 * math.exp(0.1380 * (hl - 1)), 5)
            self.label_collision_history_risk_index_initial.setNum(result)
        elif inspection_details_gcws_type == 'Active' and (gcws_observe_gates_n_or_e_approach == 'Yes' or gcws_observe_gates_s_or_w_approach == 'Yes'):
            result = round(0.001088 * ((c * t + 0.2)/0.2)**0.3116 * math.exp(0.2912 * mt) * 1 * 1 * 1 * 1 * math.exp(0.1036 * (hl - 1)) ,5)
            self.label_collision_history_risk_index_initial.setNum(result)
        else:
            result = 'No Value'
            self.label_collision_history_risk_index_initial.setText(result)

        return result
    
    #Calculate collision_history_risk_index_final
    def handle_collision_history_risk_index_final(self, name, value):
        print('handle_collision_history_risk_index_final', name, value)

        collision_history_risk_index_initial = self.handle_collision_history_risk_index_initial(name, value)
        collision_history_total_5_year_period = self.handle_collision_history_total_5_year_period(name, value)

        print('collision_history_risk_index_initial', collision_history_risk_index_initial, type(collision_history_risk_index_initial))
        print('collision_history_total_5_year_period', collision_history_total_5_year_period, type(collision_history_total_5_year_period))

        if collision_history_risk_index_initial == 'No Value':
            result = 'No Value'
            self.label_collision_history_risk_index_final.setText(result)
        else:
            result = round(
                sum([ 
                (1/sum([0.05,collision_history_risk_index_initial])) * collision_history_risk_index_initial / sum([5, 1 / sum([0.05, collision_history_risk_index_initial])]),
                collision_history_total_5_year_period / sum([5, 1 / sum([0.05, collision_history_risk_index_initial])])
                ]),
                5)
            print('result', result)
            self.label_collision_history_risk_index_final.setNum(result)
        return result

    #Calculate general_info_rail_no_tracks_total
    def handle_general_info_rail_no_tracks_total(self, name, value):
        print('handle_general_info_rail_no_tracks_total', name, value)
        
        general_info_rail_no_tracks_main = self.spinBox_general_info_rail_no_tracks_main.value()
        general_info_rail_no_tracks_other = self.spinBox_general_info_rail_no_tracks_other.value()
        
        result = sum([general_info_rail_no_tracks_main, general_info_rail_no_tracks_other])
        self.label_general_info_rail_no_tracks_total.setNum(result)
        return result

    #Calculate general_info_rail_no_trains_per_day_total
    def handle_general_info_rail_no_trains_per_day_total(self, name, value):
        print('handle_general_info_rail_no_trains_per_day_total', name, value)
        
        general_info_rail_no_trains_per_day_freight = self.spinBox_general_info_rail_no_trains_per_day_freight.value()
        general_info_rail_no_trains_per_day_passengers = self.spinBox_general_info_rail_no_trains_per_day_passengers.value()
        
        result = sum([general_info_rail_no_trains_per_day_freight, general_info_rail_no_trains_per_day_passengers])
        self.label_general_info_rail_no_trains_per_day_total.setNum(result)
        return result

    #Calculate general_info_road_no_traffic_lanes_total
    def handle_general_info_road_no_traffic_lanes_total(self, name, value):
        print('handle_general_info_road_no_traffic_lanes_total', name, value)
        
        general_info_road_no_traffic_lanes_bidirectional = self.spinBox_general_info_road_no_traffic_lanes_bidirectional.value()
        general_info_road_no_traffic_lanes_northbound_or_eastbound = self.spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound.value()
        general_info_road_no_traffic_lanes_southbound_or_westbound = self.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound.value()        
        
        result = sum([general_info_road_no_traffic_lanes_bidirectional, general_info_road_no_traffic_lanes_northbound_or_eastbound, general_info_road_no_traffic_lanes_southbound_or_westbound])
        self.label_general_info_road_no_traffic_lanes_total.setNum(result)
        return result

    #Calculate general_info_rail_railway_design_speed
    def handle_general_info_rail_railway_design_speed(self, name, value):
        print('handle_general_info_rail_railway_design_speed', name, value)

        general_info_rail_max_railway_operating_speed_freight = self.spinBox_general_info_rail_max_railway_operating_speed_freight.value()
        general_info_rail_max_railway_operating_speed_passenger = self.spinBox_general_info_rail_max_railway_operating_speed_passenger.value()        
        
        result = max((general_info_rail_max_railway_operating_speed_freight, general_info_rail_max_railway_operating_speed_passenger))
        self.label_general_info_rail_railway_design_speed.setNum(result)
        return result

    # DESIGN CONSIDERATIONS (GCS SECTION 10)
    #Calculate design_calculate_adjacent_track_clearance_time
    def handle_design_calculate_adjacent_track_clearance_time(self, name, value):
        print('handle_design_calculate_adjacent_track_clearance_time', name, value)
        
        design_measure_adjacent_track_separation_distance = self.doubleSpinBox_design_measure_adjacent_track_separation_distance.value()
        design_measure_adjacent_track_clearance_distance = self.doubleSpinBox_design_measure_adjacent_track_clearance_distance.value()

        if design_measure_adjacent_track_separation_distance<30.0 or design_measure_adjacent_track_separation_distance>60.0:
            result = "N/A"
            self.label_design_calculate_adjacent_track_clearance_time.setText(result)
        elif design_measure_adjacent_track_separation_distance>=30.0 and design_measure_adjacent_track_separation_distance<=60.0:
            result = math.ceil(sum([20.00,max(0.00,design_measure_adjacent_track_clearance_distance-10.668)/3.048]))
            self.label_design_calculate_adjacent_track_clearance_time.setNum(result)
        return result

    #Calculate design_calculate_clearance_time_pedestrian_design_check
    def handle_design_calculate_clearance_time_pedestrian_design_check(self, name, value):
        print('handle_design_calculate_clearance_time_pedestrian_design_check', name, value)
        
        design_measure_clearance_distance_pedestrian = self.doubleSpinBox_design_measure_clearance_distance_pedestrian.value()
        
        result = math.ceil(design_measure_clearance_distance_pedestrian/1.22)
        self.label_design_calculate_clearance_time_pedestrian_design_check.setNum(result)
        return result

    #Calculate design_calculate_clearance_time_vehicle_design_check
    def handle_design_calculate_clearance_time_vehicle_design_check(self, name, value):
        print('handle_design_calculate_clearance_time_pedestrian_design_check', name, value)
        
        design_input_reaction_time = self.label_design_input_reaction_time.text()
        design_calculate_vehicle_departure_time_grade_adjusted = self.handle_design_calculate_vehicle_departure_time_grade_adjusted(name, value)
        
        if design_calculate_vehicle_departure_time_grade_adjusted == 'N/A':
            result = 'N/A'
            self.label_design_calculate_clearance_time_vehicle_design_check.setText(result)
        elif design_calculate_vehicle_departure_time_grade_adjusted == 'No Value':
            result = 'No Value'
            self.label_design_calculate_clearance_time_vehicle_design_check.setText(result)
        else:
            design_input_reaction_time = float(design_input_reaction_time)
            design_calculate_vehicle_departure_time_crossing_grade_adjusted = float(design_calculate_vehicle_departure_time_grade_adjusted)
            result = math.ceil(sum([design_input_reaction_time,design_calculate_vehicle_departure_time_crossing_grade_adjusted]))
            self.label_design_calculate_clearance_time_vehicle_design_check.setNum(result)
        return result

    #TODO
    #Calculate design_calculate_gate_arm_clearance_time_pedestrian
    def handle_design_calculate_gate_arm_clearance_time_pedestrian(self, name, value):
        pass

    #Calculate design_calculate_gate_arm_clearance_time_vehicle_ssd
    def handle_design_calculate_gate_arm_clearance_time_vehicle_ssd(self, name, value):
        print('handle_design_calculate_gate_arm_clearance_time_vehicle_ssd', name, value)
        
        general_info_road_speed_design = self.spinBox_general_info_road_speed_design.value()
        design_road_design_vehicle_type = self.comboBox_design_road_design_vehicle_type.currentText()
        design_lookup_design_vehicle_length = self.handle_design_lookup_design_vehicle_length(name, value)
        sightlines_lookup_ssd_minimum_n_or_e_approach = self.handle_sightlines_lookup_ssd_minimum_n_or_e_approach(name, value)
        sightlines_lookup_ssd_minimum_s_or_w_approach = self.handle_sightlines_lookup_ssd_minimum_s_or_w_approach(name, value)

        if design_road_design_vehicle_type == "Pedestrian Only":
            result = "N/A"
            self.label_design_calculate_gate_arm_clearance_time_vehicle_ssd.setText(result)
        elif design_road_design_vehicle_type == '' or design_lookup_design_vehicle_length == "No Value" or sightlines_lookup_ssd_minimum_n_or_e_approach == "No Value" or sightlines_lookup_ssd_minimum_s_or_w_approach == "No Value" or general_info_road_speed_design == 0:
            result = "No Value"
            self.label_design_calculate_gate_arm_clearance_time_vehicle_ssd.setText(result)
        else:
            design_lookup_design_vehicle_length = float(design_lookup_design_vehicle_length)
            sightlines_lookup_ssd_minimum_n_or_e_approach = float(sightlines_lookup_ssd_minimum_n_or_e_approach)
            sightlines_lookup_ssd_minimum_s_or_w_approach = float(sightlines_lookup_ssd_minimum_s_or_w_approach)
            result = math.ceil(sum([max(sightlines_lookup_ssd_minimum_n_or_e_approach, sightlines_lookup_ssd_minimum_s_or_w_approach), 2.0, design_lookup_design_vehicle_length]) / (0.278 * general_info_road_speed_design))
            self.label_design_calculate_gate_arm_clearance_time_vehicle_ssd.setNum(result)
        return result

    #Calculate design_calculate_gate_arm_clearance_time_vehicle_stop
    def handle_design_calculate_gate_arm_clearance_time_vehicle_stop(self, name, value):
        print('handle_design_calculate_gate_arm_clearance_time_vehicle_stop', name, value)
        
        design_input_reaction_time = self.label_design_input_reaction_time.text()
        design_lookup_grade_adjustment_factor = self.handle_design_lookup_grade_adjustment_factor(name, value)
        design_calculate_vehicle_departure_time_gate_arm_clearance = self.handle_design_calculate_vehicle_departure_time_gate_arm_clearance(name, value)

        if design_calculate_vehicle_departure_time_gate_arm_clearance == 'N/A' or design_lookup_grade_adjustment_factor == 'N/A':
            result = 'N/A'
            self.label_design_calculate_gate_arm_clearance_time_vehicle_stop.setText(result)
        elif design_calculate_vehicle_departure_time_gate_arm_clearance == 'No Value' or design_lookup_grade_adjustment_factor == 'No Value':
            result = 'No Value'
            self.label_design_calculate_gate_arm_clearance_time_vehicle_stop.setText(result)
        else:
            design_input_reaction_time = float(design_input_reaction_time)
            design_calculate_vehicle_departure_time_gate_arm_clearance = float(design_calculate_vehicle_departure_time_gate_arm_clearance)
            design_lookup_grade_adjustment_factor = float(design_lookup_grade_adjustment_factor)
            result = math.ceil(sum([design_input_reaction_time, design_calculate_vehicle_departure_time_gate_arm_clearance * design_lookup_grade_adjustment_factor]))
            self.label_design_calculate_gate_arm_clearance_time_vehicle_stop.setNum(result)
        return result

    #Calculate design_calculate_gate_arm_clearance_time_vehicle_recommended
    def handle_design_calculate_gate_arm_clearance_time_vehicle_recommended(self, name, value):
        print('handle_design_calculate_gate_arm_clearance_time_vehicle_recommended', name, value)
        
        design_calculate_gate_arm_clearance_time_vehicle_ssd = self.handle_design_calculate_gate_arm_clearance_time_vehicle_ssd(name, value)
        design_calculate_gate_arm_clearance_time_vehicle_stop = self.handle_design_calculate_gate_arm_clearance_time_vehicle_stop(name, value)

        if design_calculate_gate_arm_clearance_time_vehicle_ssd == 'N/A' or design_calculate_gate_arm_clearance_time_vehicle_stop == 'N/A':
            result = 'N/A'
            self.label_design_calculate_gate_arm_clearance_time_vehicle_recommended.setText(result)
        elif design_calculate_gate_arm_clearance_time_vehicle_ssd == 'No Value' or design_calculate_gate_arm_clearance_time_vehicle_ssd == 'No Value':
            result = 'No Value'
            self.label_design_calculate_gate_arm_clearance_time_vehicle_recommended.setText(result)
        else:
            design_calculate_clearance_time_gate_arm_ssd = int(design_calculate_gate_arm_clearance_time_vehicle_ssd)
            design_calculate_clearance_time_gate_arm_stop = int(design_calculate_gate_arm_clearance_time_vehicle_ssd)
            result = max(design_calculate_clearance_time_gate_arm_ssd, design_calculate_clearance_time_gate_arm_stop)
            self.label_design_calculate_gate_arm_clearance_time_vehicle_recommended.setNum(result)
        return result

    #Calulcate design_calculate_vehicle_departure_time
    def handle_design_calculate_vehicle_departure_time(self, name, value):
        print('handle_design_calculate_vehicle_departure_time', name, value)

        design_measure_clearance_distance_pedestrian = self.doubleSpinBox_design_measure_clearance_distance_pedestrian.value()
        design_calculate_vehicle_travel_distance = self.handle_design_calculate_vehicle_travel_distance(name, value)
        design_lookup_design_vehicle_class = self.handle_design_lookup_design_vehicle_class(name, value)
        
        if design_lookup_design_vehicle_class == 'Pedestrian':
            result = 'N/A'
            self.label_design_calculate_vehicle_departure_time.setText(result)
        elif design_lookup_design_vehicle_class == 'No Value' or design_calculate_vehicle_travel_distance == 'No Value':
            result = 'No Value'
            self.label_design_calculate_vehicle_departure_time.setText(result)
        elif design_lookup_design_vehicle_class == 'Cars' and design_calculate_vehicle_travel_distance != 'No Value':
            design_calculate_vehicle_travel_distance = float(design_calculate_vehicle_travel_distance)
            result = round(max(4.00,-1.83359063314625E-07 * design_calculate_vehicle_travel_distance**4 + 0.000030862217902978 * design_calculate_vehicle_travel_distance**3 - 0.00243559236227734 * design_calculate_vehicle_travel_distance**2 + 0.194096256511465 * design_calculate_vehicle_travel_distance + 1.9653478726958),4)
            self.label_design_calculate_vehicle_departure_time.setNum(result)
        elif design_lookup_design_vehicle_class == 'Single-Unit Trucks' and design_calculate_vehicle_travel_distance != 'No Value':
            design_calculate_vehicle_travel_distance = float(design_calculate_vehicle_travel_distance)
            result = round(max(6.00,2.95895110935529E-06 * design_calculate_vehicle_travel_distance**3 - 0.00120538991988588 * design_calculate_vehicle_travel_distance**2 + 0.23080739982193 * design_calculate_vehicle_travel_distance + 3.11489082547138),4)
            self.label_design_calculate_vehicle_departure_time.setNum(result)
        elif (design_lookup_design_vehicle_class == 'Tractor Trailers' or design_lookup_design_vehicle_class == 'Combination Vehicles' or design_lookup_design_vehicle_class == 'Buses') and design_calculate_vehicle_travel_distance != 'No Value':
            design_calculate_vehicle_travel_distance = float(design_calculate_vehicle_travel_distance)
            result = round(max(7.00,2.43585710133203E-07 * design_calculate_vehicle_travel_distance**4 - 0.0000473118786681759 * design_calculate_vehicle_travel_distance**3 + 0.00169819852156627 * design_calculate_vehicle_travel_distance**2 + 0.211550565362998 * design_calculate_vehicle_travel_distance + 3.96662867415871),4)
            self.label_design_calculate_vehicle_departure_time.setNum(result)        
        elif design_lookup_design_vehicle_class == 'Pedestrian' and design_calculate_vehicle_travel_distance != 'No Value':
            result = round(design_measure_clearance_distance_pedestrian/1.22,4)
            self.label_design_calculate_vehicle_departure_time.setNum(result)
        return result

    #Calculate design_calculate_vehicle_departure_time_grade_adjusted
    def handle_design_calculate_vehicle_departure_time_grade_adjusted(self, name, value):
        print('handle_design_calculate_vehicle_departure_time_grade_adjusted', name, value)
        
        design_calculate_vehicle_departure_time = self.handle_design_calculate_vehicle_departure_time(name, value)
        design_lookup_grade_adjustment_factor = self.handle_design_lookup_grade_adjustment_factor(name, value)

        if design_calculate_vehicle_departure_time == 'N/A':
            result = 'N/A'
            self.label_design_calculate_vehicle_departure_time_grade_adjusted.setText(result)
        elif design_calculate_vehicle_departure_time == 'No Value' or design_lookup_grade_adjustment_factor == 'No Value':
            result = 'No Value'
            self.label_design_calculate_vehicle_departure_time_grade_adjusted.setText(result)
        else:
            design_lookup_vehicle_departure_time = float(design_calculate_vehicle_departure_time)
            design_lookup_grade_adjustment_factor = float(design_lookup_grade_adjustment_factor)
            result = design_lookup_vehicle_departure_time * design_lookup_grade_adjustment_factor
            self.label_design_calculate_vehicle_departure_time_grade_adjusted.setNum(result)
        return result

    #Calculate design_calculate_vehicle_departure_time_gate_arm_clearance
    def handle_design_calculate_vehicle_departure_time_gate_arm_clearance(self, name, value):
        print('handle_design_calculate_vehicle_departure_time_gate_arm_clearance', name, value)
        
        design_lookup_design_vehicle_class = self.handle_design_lookup_design_vehicle_class(name, value)
        design_lookup_design_vehicle_length = self.handle_design_lookup_design_vehicle_length(name, value)

        if design_lookup_design_vehicle_class == 'Pedestrian':
            result = 'N/A'
            self.label_design_calculate_vehicle_departure_time_gate_arm_clearance.setText(result)
        elif design_lookup_design_vehicle_class == 'No Value' or design_lookup_design_vehicle_length == 'No Value':
            result = 'No Value'
            self.label_design_calculate_vehicle_departure_time_gate_arm_clearance.setText(result)
        elif design_lookup_design_vehicle_class == 'Cars' and design_lookup_design_vehicle_length != 'No Value':
            design_lookup_design_vehicle_length = float(design_lookup_design_vehicle_length)
            result = round(max(4.00,-1.83359063314625E-07 * sum([design_lookup_design_vehicle_length,2.00])**4 + 0.000030862217902978 * sum([design_lookup_design_vehicle_length,2.00])**3 - 0.00243559236227073 * sum([design_lookup_design_vehicle_length,2.00])**2 + 0.194096256511465 * sum([design_lookup_design_vehicle_length,2.00]) + 1.9653478726958),4)
            self.label_design_calculate_vehicle_departure_time_gate_arm_clearance.setNum(result)
        elif design_lookup_design_vehicle_class == 'Single-Unit Trucks' and design_lookup_design_vehicle_length != 'No Value':            
            design_lookup_design_vehicle_length = float(design_lookup_design_vehicle_length)
            result = round(max(6.00,2.95895110935529E-06 * sum([design_lookup_design_vehicle_length,2.00])**3 - 0.00120538991988588 * sum([design_lookup_design_vehicle_length,2.00])**2 + 0.23080739982193 * sum([design_lookup_design_vehicle_length,2.00]) + 3.11489082547138),4)
            self.label_design_calculate_vehicle_departure_time_gate_arm_clearance.setNum(result)
        elif (design_lookup_design_vehicle_class == 'Tractor Trailers' or design_lookup_design_vehicle_class == 'Combination Vehicles' or design_lookup_design_vehicle_class == 'Buses') and design_lookup_design_vehicle_length != 'No Value':
            design_lookup_design_vehicle_length = float(design_lookup_design_vehicle_length)
            result = round(max(7.00,2.43585710133203E-07 * sum([design_lookup_design_vehicle_length,2.00])**4 - 0.0000473118786681759 * sum([design_lookup_design_vehicle_length,2.00])**3 + 0.00169819852156627 * sum([design_lookup_design_vehicle_length,2.00])**2 + 0.211550565362998 * sum([design_lookup_design_vehicle_length,2.00]) + 3.96662867415871),4)
            self.label_design_calculate_vehicle_departure_time_gate_arm_clearance.setNum(result)
        return result

    #Calculate design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted
    def handle_design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted(self, name, value):
        print('handle_design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted', name, value)
        
        design_calculate_vehicle_departure_time_gate_arm_clearance = self.handle_design_calculate_vehicle_departure_time_gate_arm_clearance(name, value)
        design_lookup_grade_adjustment_factor = self.handle_design_lookup_grade_adjustment_factor(name, value)

        if design_calculate_vehicle_departure_time_gate_arm_clearance == 'N/A':
            result = 'N/A'
            self.label_design_calculate_vehicle_departure_time_grade_adjusted.setText(result)
        elif design_calculate_vehicle_departure_time_gate_arm_clearance == 'No Value' or design_lookup_grade_adjustment_factor == 'No Value':
            result = 'No Value'
            self.label_design_calculate_vehicle_departure_time_grade_adjusted.setText(result)
        else:
            design_calculate_vehicle_departure_time_gate_arm_clearance = float(design_calculate_vehicle_departure_time_gate_arm_clearance)
            design_lookup_grade_adjustment_factor = float(design_lookup_grade_adjustment_factor)
            result = design_calculate_vehicle_departure_time_gate_arm_clearance * design_lookup_grade_adjustment_factor
            self.label_design_calculate_vehicle_departure_time_grade_adjusted.setNum(result)
        return result

    #Calculate design_calculate_vehicle_travel_distance
    def handle_design_calculate_vehicle_travel_distance(self, name, value):
        print('handle_design_calculate_vehicle_travel_distance', name, value)
        
        design_measure_clearance_distance_vehicle = self.doubleSpinBox_design_measure_clearance_distance_vehicle.value()
        design_road_design_vehicle_type = self.comboBox_design_road_design_vehicle_type.currentText()
        design_lookup_design_vehicle_length = self.handle_design_lookup_design_vehicle_length(name, value)

        if design_road_design_vehicle_type == 'Pedestrian Only':
            result = 'N/A'
            self.label_design_calculate_vehicle_travel_distance.setText(result)
        elif design_measure_clearance_distance_vehicle == 0.00 or design_lookup_design_vehicle_length == 'No Value':
            result = 'No Value'
            self.label_design_calculate_vehicle_travel_distance.setText(result)
        else:
            design_lookup_design_vehicle_length = float(design_lookup_design_vehicle_length)          
            result = sum([design_measure_clearance_distance_vehicle, design_lookup_design_vehicle_length])
            self.label_design_calculate_vehicle_travel_distance.setNum(result)
        return result

    #Calculate design_lookup_design_vehicle_class
    def handle_design_lookup_design_vehicle_class(self, name, value):
        print('handle_design_lookup_design_vehicle_class', name, value)
        
        design_road_design_vehicle_type = self.comboBox_design_road_design_vehicle_type.currentText()
        df_table_4_1_general_vehicles = pd.read_csv(r'app\\resources\\data\\TC\\GCS\\table_4_1_general_vehicles.csv')

        if design_road_design_vehicle_type == '':
            result = 'No Value'
            self.label_design_lookup_design_vehicle_class.setText(result)
        else:
            result = df_table_4_1_general_vehicles.loc[df_table_4_1_general_vehicles.general_vehicle_descriptions == f'{design_road_design_vehicle_type}','class'].item()
            self.label_design_lookup_design_vehicle_class.setText(result)
        return result

    #Calculate design_lookup_design_vehicle_length
    def handle_design_lookup_design_vehicle_length(self, name, value):
        print('handle_design_lookup_design_vehicle_length', name, value)
        
        design_road_design_vehicle_type = self.comboBox_design_road_design_vehicle_type.currentText()
        df_table_4_1_general_vehicles = pd.read_csv(r'app\\resources\\data\\TC\\GCS\\table_4_1_general_vehicles.csv')
        
        if design_road_design_vehicle_type == '':
            result = 'No Value'
            self.label_design_lookup_design_vehicle_length.setText(result)
        elif design_road_design_vehicle_type == 'Pedestrian Only':
            result = 0.0
            self.label_design_lookup_design_vehicle_length.setNum(result)
        else:
            result = df_table_4_1_general_vehicles.loc[df_table_4_1_general_vehicles.general_vehicle_descriptions == f'{design_road_design_vehicle_type}','vehicle_length_m'].item()
            self.label_design_lookup_design_vehicle_length.setNum(result)
        return result

    #Calculate design_lookup_grade_adjustment_factor
    def handle_design_lookup_grade_adjustment_factor(self, name, value):
        print('handle_design_lookup_grade_adjustment_factor', name, value)
        
        design_road_max_approach_grade_within_s = self.doubleSpinBox_design_road_max_approach_grade_within_s.value()
        design_lookup_design_vehicle_class = self.handle_design_lookup_design_vehicle_class(name, value)
        df_table_4_6_ratio_of_acceleration_times_on_road_grades = pd.read_csv(r'app\\resources\\data\\TC\\GCS\\table_4_6_ratio_of_acceleration_times_on_road_grades.csv')

        if design_lookup_design_vehicle_class == 'No Value':
            result = 'No Value'
            self.label_design_lookup_grade_adjustment_factor.setText(result)
        elif design_lookup_design_vehicle_class == 'Pedestrian':
            result = 'N/A'
            self.label_design_lookup_grade_adjustment_factor.setText(result)
        elif design_road_max_approach_grade_within_s<-3:
            result = df_table_4_6_ratio_of_acceleration_times_on_road_grades.loc[df_table_4_6_ratio_of_acceleration_times_on_road_grades.grade_crossing_design_vehicle == f'{design_lookup_design_vehicle_class}','-4'].item()
            self.label_design_lookup_grade_adjustment_factor.setNum(result)
        elif design_road_max_approach_grade_within_s>=-3 and design_road_max_approach_grade_within_s<-1:
            result = df_table_4_6_ratio_of_acceleration_times_on_road_grades.loc[df_table_4_6_ratio_of_acceleration_times_on_road_grades.grade_crossing_design_vehicle == f'{design_lookup_design_vehicle_class}','-2'].item()
            self.label_design_lookup_grade_adjustment_factor.setNum(result)
        elif design_road_max_approach_grade_within_s>=-1 and design_road_max_approach_grade_within_s<=1:
            result = df_table_4_6_ratio_of_acceleration_times_on_road_grades.loc[df_table_4_6_ratio_of_acceleration_times_on_road_grades.grade_crossing_design_vehicle == f'{design_lookup_design_vehicle_class}','0'].item()
            self.label_design_lookup_grade_adjustment_factor.setNum(result)
        elif design_road_max_approach_grade_within_s>1 and design_road_max_approach_grade_within_s<=3:
            result = df_table_4_6_ratio_of_acceleration_times_on_road_grades.loc[df_table_4_6_ratio_of_acceleration_times_on_road_grades.grade_crossing_design_vehicle == f'{design_lookup_design_vehicle_class}','2'].item()
            self.label_design_lookup_grade_adjustment_factor.setNum(result)
        elif design_road_max_approach_grade_within_s>3:
            result = df_table_4_6_ratio_of_acceleration_times_on_road_grades.loc[df_table_4_6_ratio_of_acceleration_times_on_road_grades.grade_crossing_design_vehicle == f'{design_lookup_design_vehicle_class}','4'].item()
            self.label_design_lookup_grade_adjustment_factor.setNum(result)
        return result

    # ROAD GEOMETRY (GCS SECTION 6)
    #Calculate road_geometry_lookup_gradient_difference
    def handle_road_geometry_lookup_gradient_difference(self, name, value):
        print('handle_road_geometry_lookup_gradient_difference', name, value)
        
        general_info_road_classification = self.comboBox_general_info_road_classification.currentText()
        table_6_1_difference_in_gradient = pd.read_csv(r'app\\resources\\data\\TC\\GCS\\table_6_1_difference_in_gradient.csv')

        if general_info_road_classification == '':
            result = 'No Value'
            self.label_road_geometry_lookup_gradient_difference.setText(result)
        else:
            result = table_6_1_difference_in_gradient.loc[table_6_1_difference_in_gradient.classification_description == f'{general_info_road_classification}','difference_in_gradient_pct'].item()
            self.label_road_geometry_lookup_gradient_difference.setNum(result)
        return result

    # SIGHTLINES (GCS SECTION 7)
    #Calculate sightlines_lookup_existing_active_crossing
    def handle_sightlines_lookup_existing_active_crossing(self, name, value):
        print('handle_sightlines_lookup_existing_active_crossing', name, value)
        
        inspection_details_gcws_type = self.comboBox_inspection_details_gcws_type.currentText()

        if inspection_details_gcws_type == '':
            result = 'No Value'
            self.label_sightlines_lookup_existing_active_crossing.setText(result)
        elif inspection_details_gcws_type == 'Active':
            result = 'Yes'
            self.label_sightlines_lookup_existing_active_crossing.setText(result)
        else:
            result = 'No'
            self.label_sightlines_lookup_existing_active_crossing.setText(result)
        return result

    #Calculate sightlines_lookup_existing_active_crossing_with_gates
    def handle_sightlines_lookup_existing_active_crossing_with_gates(self, name, value):
        print('handle_sightlines_lookup_existing_active_crossing_with_gates', name, value)
        
        inspection_details_gcws_type = self.comboBox_inspection_details_gcws_type.currentText()
        gcws_observe_gates_n_or_e_approach = self.comboBox_gcws_observe_gates_n_or_e_approach.currentText()
        gcws_observe_gates_s_or_w_approach = self.comboBox_gcws_observe_gates_s_or_w_approach.currentText()

        if inspection_details_gcws_type == '' or (gcws_observe_gates_n_or_e_approach == '' and gcws_observe_gates_s_or_w_approach == ''):
            result = 'No Value'
            self.label_sightlines_lookup_existing_active_crossing_with_gates.setText(result)
        elif inspection_details_gcws_type == 'Active' and (gcws_observe_gates_n_or_e_approach == 'Yes' or gcws_observe_gates_s_or_w_approach == 'Yes'):
            result = 'Yes'
            self.label_sightlines_lookup_existing_active_crossing_with_gates.setText(result)
        else:
            result = 'No'
            self.label_sightlines_lookup_existing_active_crossing_with_gates.setText(result)
        return result

    #Calculate sightlines_calculate_dssd_vehicle_min_ft
    def handle_sightlines_calculate_dssd_vehicle_min_ft(self, name, value):
        print('handle_sightlines_calculate_dssd_vehicle_min_ft', name, value)

        general_info_road_speed_design = self.spinBox_general_info_road_speed_design.value()
        design_measure_clearance_distance_vehicle = self.doubleSpinBox_design_measure_clearance_distance_vehicle.value()
        design_lookup_design_vehicle_class = self.handle_design_lookup_design_vehicle_class(name, value)
        design_lookup_design_vehicle_length = self.handle_design_lookup_design_vehicle_length(name, value)
        general_info_rail_railway_design_speed = self.handle_general_info_rail_railway_design_speed(name, value)
        sightlines_lookup_ssd_minimum_n_or_e_approach = self.handle_sightlines_lookup_ssd_minimum_n_or_e_approach(name, value)
        sightlines_lookup_ssd_minimum_s_or_w_approach = self.handle_sightlines_lookup_ssd_minimum_s_or_w_approach(name, value)

        if design_lookup_design_vehicle_class == 'No Value' or general_info_rail_railway_design_speed == 'No Value' or general_info_road_speed_design == 0 or design_measure_clearance_distance_vehicle == 0.0 or sightlines_lookup_ssd_minimum_n_or_e_approach == 'No Value' or sightlines_lookup_ssd_minimum_s_or_w_approach == 'No Value' or design_lookup_design_vehicle_length == 'No Value':
            result = 'No Value'
            self.label_sightlines_calculate_dssd_vehicle_min_ft.setText(result)
        elif design_lookup_design_vehicle_class == 'Pedestrian':
            result = 'N/A'
            self.label_sightlines_calculate_dssd_vehicle_min_ft.setText(result)
        else:
            design_measure_clearance_distance_vehicle = float(design_measure_clearance_distance_vehicle)
            design_lookup_design_vehicle_length = float(design_lookup_design_vehicle_length)
            general_info_rail_railway_design_speed = int(general_info_rail_railway_design_speed)
            general_info_road_speed_design = int(general_info_road_speed_design)
            sightlines_lookup_ssd_minimum_n_or_e_approach = float(sightlines_lookup_ssd_minimum_n_or_e_approach)
            sightlines_lookup_ssd_minimum_s_or_w_approach = float(sightlines_lookup_ssd_minimum_s_or_w_approach)
            result = round(1.47 * general_info_rail_railway_design_speed * max(10,sum([max(sightlines_lookup_ssd_minimum_n_or_e_approach, sightlines_lookup_ssd_minimum_s_or_w_approach), design_measure_clearance_distance_vehicle, design_lookup_design_vehicle_length]) / (0.278* general_info_road_speed_design)), 2)
            self.label_sightlines_calculate_dssd_vehicle_min_ft.setNum(result)
        return result

    #Calculate sightlines_calculate_dssd_vehicle_min_m
    def handle_sightlines_calculate_dssd_vehicle_min_m(self, name, value):
        print('handle_sightlines_calculate_dssd_vehicle_min_m', name, value)
        
        sightlines_calculate_dssd_vehicle_min_ft = self.handle_sightlines_calculate_dssd_vehicle_min_ft(name, value)

        if sightlines_calculate_dssd_vehicle_min_ft == 'No Value':
            result = 'No Value'
            self.label_sightlines_calculate_dssd_vehicle_min_m.setText(result)
        elif sightlines_calculate_dssd_vehicle_min_ft == 'N/A':
            result = 'N/A'
            self.label_sightlines_calculate_dssd_vehicle_min_m.setText(result)
        else:
            sightlines_calculate_dssd_vehicle_min_ft = float(sightlines_calculate_dssd_vehicle_min_ft)
            result = sightlines_calculate_dssd_vehicle_min_ft * 0.3048
            self.label_sightlines_calculate_dssd_vehicle_min_m.setNum(result)
        return result

    #Calculate sightlines_calculate_dstopped_pedestrian_min_ft
    def handle_sightlines_calculate_dstopped_pedestrian_min_ft(self, name, value):
        print('handle_sightlines_calculate_dstopped_pedestrian_min_ft', name, value)
        
        design_calculate_clearance_time_crossing_pedestrian_design_check = self.handle_design_calculate_clearance_time_pedestrian_design_check(name, value)
        general_info_rail_railway_design_speed = self.handle_general_info_rail_railway_design_speed(name, value)

        if general_info_rail_railway_design_speed == 'No Value' or design_calculate_clearance_time_crossing_pedestrian_design_check == 'No Value':
            result = 'No Value'
            self.label_sightlines_calculate_dstopped_pedestrian_min_ft.setText(result)
        else:
            design_calculate_clearance_time_crossing_pedestrian_design_check = float(design_calculate_clearance_time_crossing_pedestrian_design_check)
            general_info_rail_railway_design_speed = int(general_info_rail_railway_design_speed)
            result = round(1.47 * general_info_rail_railway_design_speed * max(10, design_calculate_clearance_time_crossing_pedestrian_design_check),2)
            self.label_sightlines_calculate_dstopped_pedestrian_min_ft.setNum(result)
        return result

    #Calculate sightlines_calculate_dstopped_pedestrian_min_m
    def handle_sightlines_calculate_dstopped_pedestrian_min_m(self, name, value):
        print('handle_sightlines_calculate_dstopped_pedestrian_min_m', name, value)
        
        sightlines_calculate_dstopped_pedestrian_min_ft = self.handle_sightlines_calculate_dstopped_pedestrian_min_ft(name, value)

        if sightlines_calculate_dstopped_pedestrian_min_ft == "No Value":
            result = "No Value"
            self.label_sightlines_calculate_dstopped_pedestrian_min_m.setText(result)
        else:
            sightlines_calculate_dstopped_pedestrian_min_ft = float(sightlines_calculate_dstopped_pedestrian_min_ft)
            result = round(sightlines_calculate_dstopped_pedestrian_min_ft * 0.3048, 2)
            self.label_sightlines_calculate_dstopped_pedestrian_min_m.setNum(result)
        return result

    #Calculate sightlines_calculate_dstopped_vehicle_min_ft
    def handle_sightlines_calculate_dstopped_vehicle_min_ft(self, name, value):
        print('handle_sightlines_calculate_dstopped_vehicle_min_ft', name, value)
        
        design_calculate_clearance_time_vehicle_design_check = self.handle_design_calculate_clearance_time_vehicle_design_check(name, value)
        general_info_rail_railway_design_speed = self.handle_general_info_rail_railway_design_speed(name, value)

        if design_calculate_clearance_time_vehicle_design_check == 'N/A':
            result = 'N/A'
            self.label_sightlines_calculate_dstopped_vehicle_min_ft.setText(result)
        elif general_info_rail_railway_design_speed == 'No Value' or design_calculate_clearance_time_vehicle_design_check == 'No Value':
            result = 'No Value'
            self.label_sightlines_calculate_dstopped_vehicle_min_ft.setText(result)
        else:
            design_calculate_clearance_time_crossing_vehicle_design_check = float(design_calculate_clearance_time_vehicle_design_check)
            general_info_rail_railway_design_speed = int(general_info_rail_railway_design_speed)
            result = round(1.47 * general_info_rail_railway_design_speed * max(10, design_calculate_clearance_time_crossing_vehicle_design_check),2)
            self.label_sightlines_calculate_dstopped_vehicle_min_ft.setNum(result)
        return result

    #Calculate sightlines_calculate_dstopped_vehicle_min_m
    def handle_sightlines_calculate_dstopped_vehicle_min_m(self, name, value):
        print('handle_sightlines_calculate_dstopped_vehicle_min_m', name, value)
        
        sightlines_calculate_dstopped_vehicle_min_ft = self.handle_sightlines_calculate_dstopped_vehicle_min_ft(name, value)

        if sightlines_calculate_dstopped_vehicle_min_ft == 'N/A':
            result = "N/A"
            self.label_sightlines_calculate_dstopped_vehicle_min_m.setText(result)
        elif sightlines_calculate_dstopped_vehicle_min_ft == "No Value":
            result = "No Value"
            self.label_sightlines_calculate_dstopped_vehicle_min_m.setText(result)
        else:
            sightlines_calculate_dstopped_vehicle_min_ft = float(sightlines_calculate_dstopped_vehicle_min_ft)
            result = round(sightlines_calculate_dstopped_vehicle_min_ft * 0.3048, 2)
            self.label_sightlines_calculate_dstopped_vehicle_min_m.setNum(result)
        return result

    #Calculate sightlines_lookup_ssd_minimum_n_or_e_approach
    def handle_sightlines_lookup_ssd_minimum_n_or_e_approach(self, name, value):
        print('handle_sightlines_lookup_ssd_minimum_n_or_e_approach', name, value)

        general_info_road_speed_design = self.spinBox_general_info_road_speed_design.value()
        road_geometry_road_general_approach_grade_n_or_e_approach = self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.value()
        design_lookup_design_vehicle_class = self.handle_design_lookup_design_vehicle_class(name, value)
        df_table_4_5_SSD_m_passenger_car_class = pd.read_csv(r'app\\resources\\data\\TC\\GCS\\table_4_5_SSD_m_passenger_car_class.csv')

        road_geometry_road_general_approach_grade_n_or_e_approach = round(road_geometry_road_general_approach_grade_n_or_e_approach/100.0, 0)

        if road_geometry_road_general_approach_grade_n_or_e_approach >= 0.1:
            road_geometry_road_general_approach_grade_n_or_e_approach = 0.1
        elif road_geometry_road_general_approach_grade_n_or_e_approach <= -0.1:
            road_geometry_road_general_approach_grade_n_or_e_approach = -0.1

        if general_info_road_speed_design == '' or design_lookup_design_vehicle_class == 'No Value':
            result = 'No Value'
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setText(result)
        elif design_lookup_design_vehicle_class == 'Pedestrian':
            result = 'N/A'
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setText(result)
        elif general_info_road_speed_design>=0.0 and general_info_road_speed_design<=10:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[0, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=11 and general_info_road_speed_design<=20:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[1, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=21 and general_info_road_speed_design<=30:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[2, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=31 and general_info_road_speed_design<=40:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[3, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=41 and general_info_road_speed_design<=50:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[4, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=51 and general_info_road_speed_design<=60:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[5, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=61 and general_info_road_speed_design<=70:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[6, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=71 and general_info_road_speed_design<=80:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[7, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=81 and general_info_road_speed_design<=90:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[8, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=91 and general_info_road_speed_design<=100:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[9, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=101 and general_info_road_speed_design<=110:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[10, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        return result

    #Calculate sightlines_lookup_ssd_minimum_s_or_w_approach
    def handle_sightlines_lookup_ssd_minimum_s_or_w_approach(self, name, value):
        print('handle_sightlines_lookup_ssd_minimum_s_or_w_approach', name, value)

        general_info_road_speed_design = self.spinBox_general_info_road_speed_design.value()
        road_geometry_road_general_approach_grade_s_or_w_approach = self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.value()
        design_lookup_design_vehicle_class = self.handle_design_lookup_design_vehicle_class(name, value)
        df_table_4_5_SSD_m_passenger_car_class = pd.read_csv(r'app\\resources\\data\\TC\\GCS\\table_4_5_SSD_m_passenger_car_class.csv')

        road_geometry_road_general_approach_grade_s_or_w_approach = round(road_geometry_road_general_approach_grade_s_or_w_approach/100.0, 0)

        if road_geometry_road_general_approach_grade_s_or_w_approach >= 0.1:
            road_geometry_road_general_approach_grade_s_or_w_approach = 0.1
        elif road_geometry_road_general_approach_grade_s_or_w_approach <= -0.1:
            road_geometry_road_general_approach_grade_s_or_w_approach = -0.1
    
        if general_info_road_speed_design == '' or design_lookup_design_vehicle_class == 'No Value':
            result = 'No Value'
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setText(result)
        elif design_lookup_design_vehicle_class == 'Pedestrian':
            result = 'N/A'
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setText(result)
        elif general_info_road_speed_design>=0 and general_info_road_speed_design<=10:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[0, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=11 and general_info_road_speed_design<=20:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[1, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=21 and general_info_road_speed_design<=30:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[2, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=31 and general_info_road_speed_design<=40:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[3, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=41 and general_info_road_speed_design<=50:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[4, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=51 and general_info_road_speed_design<=60:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[5, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=61 and general_info_road_speed_design<=70:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[6, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=71 and general_info_road_speed_design<=80:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[7, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=81 and general_info_road_speed_design<=90:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[8, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=91 and general_info_road_speed_design<=100:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[9, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=101 and general_info_road_speed_design<=110:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[10, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        return result

        # GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
        #self.label_gcws_warrant_private_9_3.valueChanged.connect(self.handle_gcws_warrant_private_9_3)
        #self.label_gcws_warrant_private_9_3_1.valueChanged.connect(self.handle_gcws_warrant_private_9_3_1)
        #self.label_gcws_warrant_private_9_3_2_a.valueChanged.connect(self.handle_gcws_warrant_private_9_3_2_a)
        #self.label_gcws_warrant_private_9_3_2_b.valueChanged.connect(self.handle_gcws_warrant_private_9_3_2_b)
        #self.label_gcws_warrant_private_9_3_2_c.valueChanged.connect(self.handle_gcws_warrant_private_9_3_2_c)
        #self.label_gcws_warrant_public_9_1.valueChanged.connect(self.handle_gcws_warrant_public_9_1)
        #self.label_gcws_warrant_public_9_1_a.valueChanged.connect(self.handle_gcws_warrant_public_9_1_a)
        #self.label_gcws_warrant_public_9_1_b.valueChanged.connect(self.handle_gcws_warrant_public_9_1_b)
        #self.label_gcws_warrant_public_9_1_c.valueChanged.connect(self.handle_gcws_warrant_public_9_1_c)
        #self.label_gcws_warrant_public_9_1_d_i.valueChanged.connect(self.handle_gcws_warrant_public_9_1_d_i)
        #self.label_gcws_warrant_public_9_1_d_ii.valueChanged.connect(self.handle_gcws_warrant_public_9_1_d_ii)
        #self.label_gcws_warrant_public_9_1_d_iii.valueChanged.connect(self.handle_gcws_warrant_public_9_1_d_iii)
        #self.label_gcws_warrant_sidewalk_9_5.valueChanged.connect(self.handle_gcws_warrant_sidewalk_9_5)
        #self.label_gates_gcws_warrant_private_9_4_1_a.valueChanged.connect(self.handle_gates_gcws_warrant_private_9_4_1_a)
        #self.label_gates_gcws_warrant_private_9_4_1_b.valueChanged.connect(self.handle_gates_gcws_warrant_private_9_4_1_b)
        #self.label_gates_gcws_warrant_private_9_4_1_c.valueChanged.connect(self.handle_gates_gcws_warrant_private_9_4_1_c)
        #self.label_gates_gcws_warrant_public_9_2_1_a.valueChanged.connect(self.handle_gates_gcws_warrant_public_9_2_1_a)
        #self.label_gates_gcws_warrant_public_9_2_1_b.valueChanged.connect(self.handle_gates_gcws_warrant_public_9_2_1_b)
        #self.label_gates_gcws_warrant_public_9_2_1_c.valueChanged.connect(self.handle_gates_gcws_warrant_public_9_2_1_c)
        #self.label_gates_gcws_warrant_public_9_2_1_d.valueChanged.connect(self.handle_gates_gcws_warrant_public_9_2_1_d)
        #self.label_gates_gcws_warrant_public_9_2_1_e.valueChanged.connect(self.handle_gates_gcws_warrant_public_9_2_1_e)
        #self.label_gates_gcws_warrant_sidewalk_9_6.valueChanged.connect(self.handle_gates_gcws_warrant_sidewalk_9_6)

    # GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
    #Calculate gcws_rail_design_warning_time_clearance_distance
    def handle_gcws_rail_design_warning_time_clearance_distance(self, name, value):
        print('handle_gcws_rail_design_warning_time_clearance_distance', name, value)

        design_road_design_vehicle_type = self.comboBox_design_road_design_vehicle_type.currentText()
        design_measure_clearance_distance_pedestrian = self.doubleSpinBox_design_measure_clearance_distance_pedestrian.value()
        design_measure_clearance_distance_vehicle = self.doubleSpinBox_design_measure_clearance_distance_vehicle.value()

        if design_road_design_vehicle_type == '' or (design_measure_clearance_distance_pedestrian == 0.0 and design_measure_clearance_distance_vehicle == 0.0):
            result = 'No Value'
            self.label_gcws_rail_design_warning_time_clearance_distance.setText(result)
        elif design_road_design_vehicle_type == 'Pedestrian Only' and design_measure_clearance_distance_pedestrian != 0.0:
            result = math.ceil(max(20, sum([20, math.ceil(design_measure_clearance_distance_pedestrian - 11.0) / 3.0])))
            self.label_gcws_rail_design_warning_time_clearance_distance.setNum(result)
        else:
            result = math.ceil(max(20, sum([20, math.ceil(design_measure_clearance_distance_vehicle - 11.0) / 3.0])))
            self.label_gcws_rail_design_warning_time_clearance_distance.setNum(result)
        return result
    
    #Calculate gcws_rail_design_warning_time_departure_time_vehicle
    def handle_gcws_rail_design_warning_time_departure_time_vehicle(self, name, value):
        print('handle_gcws_rail_design_warning_time_departure_time_vehicle', name, value)

        design_calculate_clearance_time_vehicle_design_check = self.handle_design_calculate_clearance_time_vehicle_design_check(name, value)

        if design_calculate_clearance_time_vehicle_design_check == 'N/A':
            result = 'N/A'
            self.label_gcws_rail_design_warning_time_departure_time_vehicle.setText(result)
        elif design_calculate_clearance_time_vehicle_design_check == 'No Value':
            result = 'No Value'
            self.label_gcws_rail_design_warning_time_departure_time_vehicle.setText(result)
        else:
            design_calculate_clearance_time_crossing_vehicle_design_check = float(design_calculate_clearance_time_vehicle_design_check)
            result = math.ceil(design_calculate_clearance_time_crossing_vehicle_design_check)
            self.label_gcws_rail_design_warning_time_departure_time_vehicle.setNum(result)
        return result

    #Calculate gcws_rail_design_warning_time_departure_time_pedestrian
    def handle_gcws_rail_design_warning_time_departure_time_pedestrian(self, name, value):
        print('handle_gcws_rail_design_warning_time_departure_time_pedestrian', name, value)
        
        design_calculate_clearance_time_crossing_pedestrian_design_check = self.handle_design_calculate_clearance_time_pedestrian_design_check(name, value)

        if design_calculate_clearance_time_crossing_pedestrian_design_check == 'No Value':
            result = 'No Value'
            self.label_gcws_rail_design_warning_time_departure_time_pedestrian.setText(result)
        else:
            design_calculate_clearance_time_crossing_pedestrian_design_check = float(design_calculate_clearance_time_crossing_pedestrian_design_check)
            result = math.ceil(design_calculate_clearance_time_crossing_pedestrian_design_check)
            self.label_gcws_rail_design_warning_time_departure_time_pedestrian.setNum(result)
        return result

    #TODO
    #Calculate gcws_rail_design_warning_time_gate_arm_clearance
    def handle_gcws_rail_design_warning_time_gate_arm_clearance(self, name, value):
        print('handle_gcws_rail_design_warning_time_gate_arm_clearance', name, value)
        
        design_calculate_gate_arm_clearance_time_vehicle_recommended = self.handle_design_calculate_gate_arm_clearance_time_vehicle_recommended(name, value)
        gates_gcws_rail_gate_arm_descent_time_design = self.doubleSpinBox_gates_gcws_rail_gate_arm_descent_time_design.value()

        if design_calculate_gate_arm_clearance_time_vehicle_recommended == 'No Value' or gates_gcws_rail_gate_arm_descent_time_design == 0.0:
            result = 'No Value'
            self.label_gcws_rail_design_warning_time_gate_arm_clearance.setText(result)
        else:
            result = math.ceil(sum([design_calculate_gate_arm_clearance_time_vehicle_recommended, gates_gcws_rail_gate_arm_descent_time_design, 5.0]))
            self.label_gcws_rail_design_warning_time_gate_arm_clearance.setNum(result)
        return result

    #TODO
    #Calculate gcws_rail_design_warning_time_ssd
    def handle_gcws_rail_design_warning_time_ssd(self, name, value):
        print('handle_gcws_rail_design_warning_time_ssd', name, value)
        
        sightlines_lookup_ssd_minimum_n_or_e_approach = self.handle_sightlines_lookup_ssd_minimum_n_or_e_approach(name, value)
        sightlines_lookup_ssd_minimum_s_or_w_approach = self.handle_sightlines_lookup_ssd_minimum_s_or_w_approach(name, value)
        design_road_design_vehicle_type = self.comboBox_design_road_design_vehicle_type.currentText()
        design_calculate_vehicle_travel_distance = self.handle_design_calculate_vehicle_travel_distance(name, value)
        general_info_road_speed_design = self.spinBox_general_info_road_speed_design.value()

        if sightlines_lookup_ssd_minimum_n_or_e_approach == 'No Value' or sightlines_lookup_ssd_minimum_s_or_w_approach == 'No Value' or design_road_design_vehicle_type == '' or design_calculate_vehicle_travel_distance == 'No Value' or general_info_road_speed_design == 0:
            result = 'No Value'
            self.label_gcws_rail_design_warning_time_ssd.setText(result)
        elif design_road_design_vehicle_type == 'Pedestrian Only':
            result = 'N/A'
            self.label_gcws_rail_design_warning_time_ssd.setText(result)
        else:
            result = math.ceil(sum([max(sightlines_lookup_ssd_minimum_n_or_e_approach, sightlines_lookup_ssd_minimum_s_or_w_approach), design_calculate_vehicle_travel_distance]) * 3600 / (general_info_road_speed_design * 10**3))
            self.label_gcws_rail_design_warning_time_ssd.setNum(result)
        return result
    
    #TODO
    #Calculate gcws_rail_design_warning_time_adjacent_crossing
    def handle_gcws_rail_design_warning_time_adjacent_crossing(self, name, value):
        pass
    
    #TODO
    #Calculate gcws_rail_design_approach_warning_time
    def handle_gcws_rail_design_approach_warning_time(self, name, value):
        pass
        print('handle_gcws_rail_design_approach_warning_time', name, value)

        gcws_rail_design_warning_time_preemption = self.spinBox_gcws_rail_design_warning_time_preemption.value()
        gcws_rail_design_warning_time_clearance_distance = self.handle_gcws_rail_design_warning_time_clearance_distance(name, value)
        gcws_rail_design_warning_time_departure_time_vehicle = self.handle_gcws_rail_design_warning_time_departure_time_vehicle(name, value)
        gcws_rail_design_warning_time_departure_time_pedestrian = self.handle_gcws_rail_design_warning_time_departure_time_pedestrian(name, value)
        gcws_rail_design_warning_time_gate_arm_clearance = self.handle_gcws_rail_design_warning_time_gate_arm_clearance(name, value) 
        gcws_rail_design_warning_time_ssd = self.handle_gcws_rail_design_warning_time_ssd(name, value)

        gcws_rail_design_approach_warning_time = {
            'gcws_rail_design_warning_time_preemption': gcws_rail_design_warning_time_preemption,
            'gcws_rail_design_warning_time_clearance_distance': gcws_rail_design_warning_time_clearance_distance, 
            'gcws_rail_design_warning_time_departure_time_vehicle': gcws_rail_design_warning_time_departure_time_vehicle, 
            'gcws_rail_design_warning_time_departure_time_pedestrian': gcws_rail_design_warning_time_departure_time_pedestrian,
            'gcws_rail_design_warning_time_gate_arm_clearance': gcws_rail_design_warning_time_gate_arm_clearance, 
            'gcws_rail_design_warning_time_ssd': gcws_rail_design_warning_time_ssd
        }
         
        #for i in gcws_rail_design_approach_warning_time:
        #    print (i)

        #return gcws_rail_design_approach_warning_time

    # GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
    #TODO
    #Calculate gates_gcws_calculate_inner_gate_arm_delay_time_recommended
    def handle_gates_gcws_calculate_inner_gate_arm_delay_time_recommended(self, name, value):
        print('handle_gcws_rail_design_warning_time_ssd', name, value)
        
        design_calculate_adjacent_track_clearance_time = self.handle_design_calculate_adjacent_track_clearance_time(name, value)

        if design_calculate_adjacent_track_clearance_time == 'No Value':
            result = design_calculate_adjacent_track_clearance_time
            self.label_gcws_rail_design_warning_time_ssd.setText(result)
        else:
            result = design_calculate_adjacent_track_clearance_time
            self.label_gcws_rail_design_warning_time_ssd.setNum(result)  
        return result

    # PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
    #TODO
    #Calculate aawd_calculate_advance_activation_time_design_n_or_e_approach
    def handle_aawd_calculate_advance_activation_time_design_n_or_e_approach(self, name, value):
        print('handle_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended', name, value)

        general_info_road_speed_design = self.spinBox_general_info_road_speed_design.value()
        design_calculate_vehicle_travel_distance = self.handle_design_calculate_vehicle_travel_distance(name, value)
        aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended = self.handle_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended(name, value)

        if general_info_road_speed_design == 0 or design_calculate_vehicle_travel_distance == "No Value" or aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended == "No Value":
            result = "No Value"
            self.label_aawd_calculate_advance_activation_time_design_n_or_e_approach.setText(result)
        else:
            result = round(3.6 * sum([design_calculate_vehicle_travel_distance, aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended]) / general_info_road_speed_design, 2)
            self.label_aawd_calculate_advance_activation_time_design_n_or_e_approach.setNum(result)
        return result

    #TODO
    #Calculate aawd_calculate_advance_activation_time_design_s_or_w_approach    
    def handle_aawd_calculate_advance_activation_time_design_s_or_w_approach(self, name, value):
        print('handle_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended', name, value)

        general_info_road_speed_design = self.spinBox_general_info_road_speed_design.value()
        design_calculate_vehicle_travel_distance = self.handle_design_calculate_vehicle_travel_distance(name, value)
        aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended = self.handle_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended(name, value)

        if general_info_road_speed_design == 0 or design_calculate_vehicle_travel_distance == 'No Value' or aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended == 'No Value':
            result = 'No Value'
            self.label_aawd_calculate_advance_activation_time_design_n_or_e_approach.setText(result)
        else:
            result = round(3.6 * sum([design_calculate_vehicle_travel_distance, aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended]) / general_info_road_speed_design, 2)
            self.label_aawd_calculate_advance_activation_time_design_n_or_e_approach.setNum(result)
        return result

    #TODO
    #Calculate aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended
    def handle_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended(self, name, value):
        print('handle_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended', name, value)

        general_info_road_speed_posted = self.spinBox_general_info_road_speed_posted.value()
        road_geometry_road_general_approach_grade_n_or_e_approach = self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.value()
        road_geometry_road_general_approach_grade_s_or_w_approach = self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.value()
        design_input_reaction_time = self.label_design_input_reaction_time.text()
        deceleration_rate = 2.6 #typically 2.6m/s2
        gravitational_acceleration = 9.81 #typically 9.81m/s2)

        if general_info_road_speed_posted == 0 or road_geometry_road_general_approach_grade_n_or_e_approach == 0.0 or road_geometry_road_general_approach_grade_s_or_w_approach == 0.0:
            result = 'No Value'
            self.label_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended.setText(result)
        else:
            result = sum([general_info_road_speed_posted * design_input_reaction_time / 3.6, general_info_road_speed_posted**2 / (25.92 * sum([deceleration_rate, road_geometry_road_general_approach_grade_n_or_e_approach * gravitational_acceleration])) ])
            self.label_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended.setNum(result)
        return result

    #TODO
    #Calculate aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended
    def handle_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended(self, name, value):
        print('handle_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended', name, value)

        general_info_road_speed_posted = self.spinBox_general_info_road_speed_posted.value()
        road_geometry_road_general_approach_grade_n_or_e_approach = self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.value()
        road_geometry_road_general_approach_grade_s_or_w_approach = self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.value()
        design_input_reaction_time = self.label_design_input_reaction_time.text()
        deceleration_rate = 2.6 #typically 2.6m/s2
        gravitational_acceleration = 9.81 #typically 9.81m/s2)

        if general_info_road_speed_posted == 0 or road_geometry_road_general_approach_grade_n_or_e_approach == 0.0 or road_geometry_road_general_approach_grade_s_or_w_approach == 0.0:
            result = 'No Value'
            self.label_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended.setText(result)
        else:
            result = sum([general_info_road_speed_posted * design_input_reaction_time / 3.6, general_info_road_speed_posted**2 / (25.92 * sum([deceleration_rate, road_geometry_road_general_approach_grade_s_or_w_approach * gravitational_acceleration])) ])
            self.label_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended.setNum(result)
        return result

    #TODO
    #Calculate aawd_warrant_gcr_lookup_road_classification
    def handle_aawd_warrant_gcr_lookup_road_classification(self, name, value):
        print('handle_aawd_warrant_gcr_lookup_road_classification', name, value)

        general_info_road_classification = self.comboBox_general_info_road_classification.currentText()
        general_info_road_classification.split()

        if general_info_road_classification == '':
            result = 'No Value'
            self.label_aawd_warrant_gcr_lookup_road_classification.setText(result)
        elif general_info_road_classification[1] == 'Freeway':
            result = 'Yes'
            self.label_aawd_warrant_gcr_lookup_road_classification.setText(result)
        else:
            result = 'No'
            self.label_aawd_warrant_gcr_lookup_road_classification.setText(result)
        return result

    #TODO
    #Calculate aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr
    def handle_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr(self, name, value):
        pass
        #self.spinBox_general_info_road_speed_design
    
    # INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
    #TODO
    #Calculate preemption_of_traffic_signals_lookup_proximity_condition
    def preemption_of_traffic_signals_lookup_proximity_condition(self, name, value):
        pass
        #self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach
        #self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach

    #TODO
    #Calculate preemption_of_traffic_signals_lookup_required
    def preemption_of_traffic_signals_lookup_required(self, name, value):
        pass
        #self.label_general_info_rail_railway_design_speed
        #self.label_preemption_of_traffic_signals_lookup_proximity_condition

    # WHISTLE CESSATION (GCS SECTION Appendix D)
    #Group Labels
    #TODO
    #Calculate areas_without_train_whistling_lookup_gcs_9_2
    def handle_areas_without_train_whistling_lookup_gcs_9_2(self, name, value):
        pass
        #self.comboBox_gcws_observe_gates_n_or_e_approach
        #self.comboBox_gcws_observe_gates_s_or_w_approach
        #self.label_gates_gcws_warrant_public_9_2_1_a
        #self.label_gates_gcws_warrant_public_9_2_1_b
        #self.label_gates_gcws_warrant_public_9_2_1_c
        #self.label_gates_gcws_warrant_public_9_2_1_d
        #self.label_gates_gcws_warrant_public_9_2_1_e

    #TODO
    #Calculate areas_without_train_whistling_requirements_lookup_table_d1_criteria
    def handle_areas_without_train_whistling_requirements_lookup_table_d1_criteria(self, name, value):
        pass
        #self.label_general_info_rail_no_tracks_total
        #self.label_general_info_rail_railway_design_speed

    #TODO
    #Calculate areas_without_train_whistling_requirements_observe_table_D1
    def handle_areas_without_train_whistling_requirements_observe_table_D1(self, name, value):
        pass
        #self.comboBox_gcws_observe_gates_n_or_e_approach
        #self.comboBox_gcws_observe_gates_s_or_w_approach
        #self.comboBox_gcws_observe_light_units_n_or_e_approach
        #self.comboBox_gcws_observe_light_units_s_or_w_approach
        #self.label_areas_without_train_whistling_requirements_lookup_table_d1_criteria

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('Crossing Assessment Form')
        self.formWidgets()

        self.show()
    
    def formWidgets(self):
        """
        Create widgets that will be used in the application form. 
        """

        # Combo Box Lists
        list_yes_no = ['', 'Yes', 'No']
        list_yes_no_na = ['', 'Yes', 'No', 'N/A']
        list_condition = ['', 'Good', 'Fair', 'Poor']
        list_inspection_details_gcws_type = ['','Active','Passive']
        list_inspection_details_grade_crossing_type = ['','Public', 'Private (CTA 102-Type)', 'Private (CTA 103-Type)']
        list_inspection_details_track_type = ['','Mainline', 'Industrial Spur', 'Mainline Spur', 'Yard, Other']
        list_inspection_details_province = ['', 'AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'ON', 'QC', 'SK', 'YT']
        list_inspection_details_reason_for_assessment = [
            "",
            "Periodic Assessment",
            "A Significant Change in Infrastructure",
            "Whistle Cessation",
            "2+ Fatal Collisions in 5-Year Period",
            "Other Collision Experience (see below)",
            "Receipt of a notice from a Railway Company, under Section 3 of the Notice of Railway Works Regulations. Ref. (GCR 12.(2))",
            "A change in the design vehicle and the sightlines at the grade crossing, which must meet the requirements in Section 20 of the GCR. Ref. (GCR 13 GCR 28.(c))",
            "An increase in the design speed of the road crossing, which will result in a change to the road approach's classification as set out in column B of the Table 10-2 of the Grade Crossings Standards (GCS). Ref. (GCR 13 GCR 28.(d))",
            "The location, gradient or crossing angle of a grade crossing has changed, and Articles 6 and 11 of the GCS must be applied in a manner that improves the overall safety of the grade crossing. Ref. (GCR 13 GCR 88.(1))",
            "An increase of the absolute gradient of a road approach to an existing grade crossing which meets the standards set out in Article 6.3 of the GCS. Ref. (GCR 13 GCR 88.(2))",
            "The number or width of traffic lanes of a road approach increases, or a shoulder is added or a shoulder's width is increased. The grade crossing must meet the standards set out in Articles 5.1 and 6.4 of the GCS. Ref. (GCR 13 GCR 89)",
            "A traffic signal is installed at a grade crossing that corresponds to the specifications set out in Article 19.1 of the GCS, the warning system must be interconnected with the traffic signal, and the interconnection must meet the standards set out in Articles 19.2 to 19.4 of the GCS. Ref. (GCR 13 GCR 90)",
            "A change in the design vehicle, which has resulted in a change to the period of time that the warning system must operate, before railway equipment reaches the crossing surface and therefore must meet the standards set out in Article 16.1 of the GCS. Ref. (GCR 13 GCR 91)",
            "Receipt of a notice from a Road Authority under Section 3 of the Notice of Railway Works Regulations. Ref. (GCR 4.(2))",
            "A line of railway is added within the sightlines of the grade crossing and the sightlines must meet the requirements in Section 20 of the GCR. Ref. (GCR 5 – GCR 28.(a))"
            "There is a change in the class of track referred to in column 1 of the table in article 7.1.2 of the Grade Crossing Standards (GCS),  taking into account the maximum allowable operating speeds set out in column 2 or 3 of that table. Sightlines at the grade crossing must meet the requirements in Section 20 of the GCR. Ref. (GCR 5 – GCR 28.(b))",
            "A new warning system is installed at a grade crossing and must meet the applicable standards set out in Articles 12 to 16 of the GCS. Ref. (GCR 5 – GCR 87.(1))",
            "A component of a warning system is modified or installed and must meet the applicable standards set out in Articles 12 and 16 of the GCS. Ref. (GCR 5 – GCR 87.(2))",
            "A new installation of a warning system, or the modification or installation of a component of a warning system which results from an increase in the railway design speed. The warning system or component must meet the applicable standards set out in Articles 12 and 16 of the GCS before the increase in the railway design speed takes effect. Ref. (GCR 5 – GCR 87.(3))"
            ]
        list_general_info_road_classification = ['', 'Rural Local Undivided', 'Rural Collector Undivided',
            'Rural Collector Divided', 'Rural Arterial Undivided', 'Rural Arterial Divided', 'Rural Freeway Divided',
            'Urban Local Undivided', 'Urban Collector Undivided', 'Urban Collector Divided', 'Urban Arterial Undivided',
            'Urban Arterial Divided', 'Private Road', 'Pedestrian Crossing']
        list_general_info_observe_surrounding_land_use = ['', 'Farm', 'Residential', 'Recreational', 'Industrial', 'Commercial']
        list_design_road_design_vehicle_type = ['', 'Passenger Cars, Vans, and Pickups', 'Light Single-Unit Trucks',
            'Medium Single-Unit Trucks', 'Heavy Single-Unit Trucks', 'WB-19 Tractor-Semitrailers', 
            'WB-20 Tractor-Semitrailers', 'A-Train Doubles (ATD)', 'B-Train Doubles', 'Standard Single-Unit Buses (B-12)',
            'Articulated Buses (A-Bus)', 'Intercity Buses (I-Bus)', 'Pedestrian Only']
        list_grade_crossing_surface_observe_material = ['', 'Timber', 'Asphalt', 'Asphalt and Flange', 
            'Concrete', 'Concrete and Rubber', 'Rubber', 'Metal', 'Unconsolidated', 'Other']
        list_grade_crossing_surface_observe_road_approach_surface_type = ['', 'Asphalt', 'Concrete', 'Gravel']
        list_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type = ['', 'Not Interconnected', 'Advance Preemption', 'Simultaneous Preemption']
                
        # INSPECTION DETAILS
        #Group TextBoxes
        self.textEdit_inspection_details_assessment_team = qtw.QTextEdit()
        
        '''
        #Group DatePicker
        self.datetimeEdit_inspection_details_date_assessment = qtw.QDatetimeEdit(
            self,
            date=datetime.date.today(),
            calendarPopup=True,
            displayFormat='yyyy-MM-dd'
        )
        '''

        #Group LineEdits
        self.lineEdit_inspection_details_crossing_location = qtw.QLineEdit()  
        self.lineEdit_inspection_details_location_number = qtw.QLineEdit() 
        self.lineEdit_inspection_details_municipality = qtw.QLineEdit() 
        self.lineEdit_inspection_details_road_name = qtw.QLineEdit() 
        self.lineEdit_inspection_details_road_number = qtw.QLineEdit() 
        self.lineEdit_inspection_details_spur_name = qtw.QLineEdit() 

        #Group DoubleSpinBox
        self.doubleSpinBox_inspection_details_latitude = qtw.QDoubleSpinBox ()
        self.doubleSpinBox_inspection_details_latitude.setRange(-999999, 999999)
        
        self.doubleSpinBox_inspection_details_longitude = qtw.QDoubleSpinBox ()
        self.doubleSpinBox_inspection_details_longitude.setRange(-999999, 999999)
         
        self.doubleSpinBox_inspection_details_spur_mile = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_inspection_details_spur_mile.setRange(0, 999999)

        self.doubleSpinBox_inspection_details_subdivision_mile = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_inspection_details_subdivision_mile.setRange(0, 999999)

        #Group ComboBoxes
        self.comboBox_inspection_details_gcws_type = qtw.QComboBox()
        self.comboBox_inspection_details_gcws_type.addItems(list_inspection_details_gcws_type)

        self.comboBox_inspection_details_grade_crossing_type = qtw.QComboBox()
        self.comboBox_inspection_details_grade_crossing_type.addItems(list_inspection_details_grade_crossing_type)

        self.comboBox_inspection_details_province = qtw.QComboBox()
        self.comboBox_inspection_details_province.addItems(list_inspection_details_province)

        self.comboBox_inspection_details_railway_authority = qtw.QComboBox()
        #TODO create and add railway authority list 

        self.comboBox_inspection_details_reason_for_assessment = qtw.QComboBox()
        self.comboBox_inspection_details_reason_for_assessment.addItems(list_inspection_details_reason_for_assessment)
        
        self.comboBox_inspection_details_road_authority = qtw.QComboBox()
        #TODO create and add road authority list 

        self.comboBox_inspection_details_subdivision_name = qtw.QComboBox()
        #TODO create and add subdivision list 

        self.comboBox_inspection_details_track_type = qtw.QComboBox()
        self.comboBox_inspection_details_track_type.addItems(list_inspection_details_track_type)

        # COLLISION HISTORY (5 YEAR PERIOD)
        #Group TextEdits
        self.textEdit_collision_history_comments = qtw.QTextEdit()

        #Group SpinBox
        self.spinBox_collision_history_fatal_injury = qtw.QSpinBox()
        self.spinBox_collision_history_fatal_injury.setRange(0, 999999)
        
        self.spinBox_collision_history_fatalities = qtw.QSpinBox() 
        self.spinBox_collision_history_fatalities.setRange(0, 999999)

        self.spinBox_collision_history_personal_injuries = qtw.QSpinBox() 
        self.spinBox_collision_history_personal_injuries.setRange(0, 999999)
        
        self.spinBox_collision_history_personal_injury = qtw.QSpinBox() 
        self.spinBox_collision_history_personal_injury.setRange(0, 999999)

        self.spinBox_collision_history_property_damage = qtw.QSpinBox()
        self.spinBox_collision_history_property_damage.setRange(0, 999999)

        #Group Labels 
        self.label_collision_history_total_5_year_period = qtw.QLabel('No Value')
        self.label_collision_history_risk_index_initial = qtw.QLabel('No Value')
        self.label_collision_history_risk_index_final = qtw.QLabel('No Value')

        # GENERAL INFORMATION
        #Group TextEdits
        self.textEdit_general_info_comments = qtw.QTextEdit()

        #Group LineEdits
        self.lineEdit_general_info_observe_special_buildings = qtw.QLineEdit() 
        self.lineEdit_general_info_road_other_users = qtw.QLineEdit() 

        #Group SpinBox
        self.spinBox_general_info_rail_max_railway_operating_speed_freight = qtw.QSpinBox()
        self.spinBox_general_info_rail_max_railway_operating_speed_freight.setRange(0, 999999)
 
        self.spinBox_general_info_rail_max_railway_operating_speed_passenger = qtw.QSpinBox() 
        self.spinBox_general_info_rail_max_railway_operating_speed_passenger.setRange(0, 999999)

        self.spinBox_general_info_rail_no_tracks_main = qtw.QSpinBox() 
        self.spinBox_general_info_rail_no_tracks_main.setRange(0, 999999)

        self.spinBox_general_info_rail_no_tracks_other = qtw.QSpinBox()
        self.spinBox_general_info_rail_no_tracks_other.setRange(0, 999999)

        self.spinBox_general_info_rail_no_trains_per_day_freight = qtw.QSpinBox() 
        self.spinBox_general_info_rail_no_trains_per_day_freight.setRange(0, 999999)

        self.spinBox_general_info_rail_no_trains_per_day_passengers = qtw.QSpinBox() 
        self.spinBox_general_info_rail_no_trains_per_day_passengers.setRange(0, 999999)

        self.spinBox_general_info_road_aadt_current = qtw.QSpinBox()
        self.spinBox_general_info_road_aadt_current.setRange(0, 999999)

        self.spinBox_general_info_road_aadt_forecast = qtw.QSpinBox() 
        self.spinBox_general_info_road_aadt_forecast.setRange(0, 999999)

        self.spinBox_general_info_road_aadt_year_current = qtw.QSpinBox() 
        self.spinBox_general_info_road_aadt_year_current.setRange(0, 999999)

        self.spinBox_general_info_road_aadt_year_forecasted = qtw.QSpinBox() 
        self.spinBox_general_info_road_aadt_year_forecasted.setRange(0, 999999)

        self.spinBox_general_info_road_cyclist_per_day = qtw.QSpinBox()
        self.spinBox_general_info_road_cyclist_per_day.setRange(0, 999999)

        self.spinBox_general_info_road_no_traffic_lanes_bidirectional = qtw.QSpinBox() 
        self.spinBox_general_info_road_no_traffic_lanes_bidirectional.setRange(0, 100)

        self.spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound = qtw.QSpinBox() 
        self.spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound.setRange(0, 100)

        self.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound = qtw.QSpinBox()
        self.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound.setRange(0, 100)

        self.spinBox_general_info_road_other_users_daily_users = qtw.QSpinBox() 
        self.spinBox_general_info_road_other_users_daily_users.setRange(0, 999999)

        self.spinBox_general_info_road_pedestrians_per_day = qtw.QSpinBox() 
        self.spinBox_general_info_road_pedestrians_per_day.setRange(0, 999999)

        self.spinBox_general_info_road_speed_design = qtw.QSpinBox() 
        self.spinBox_general_info_road_speed_design.setRange(0, 200)

        self.spinBox_general_info_road_speed_posted = qtw.QSpinBox() 
        self.spinBox_general_info_road_speed_posted.setRange(0, 200)

        #Group ComboBoxes
        self.comboBox_general_info_observe_roadway_illumination = qtw.QComboBox()
        self.comboBox_general_info_observe_roadway_illumination.addItems(list_yes_no)

        self.comboBox_general_info_observe_surrounding_land_use = qtw.QComboBox()
        self.comboBox_general_info_observe_surrounding_land_use.addItems(list_general_info_observe_surrounding_land_use)

        self.comboBox_general_info_rail_train_switching = qtw.QComboBox()
        self.comboBox_general_info_rail_train_switching.addItems(list_yes_no)
        
        self.comboBox_general_info_road_assistive_pedestrian_devices = qtw.QComboBox()
        self.comboBox_general_info_road_assistive_pedestrian_devices.addItems(list_yes_no)

        self.comboBox_general_info_road_classification = qtw.QComboBox()
        self.comboBox_general_info_road_classification.addItems(list_general_info_road_classification)
        
        self.comboBox_general_info_road_dangerous_goods_route = qtw.QComboBox()
        self.comboBox_general_info_road_dangerous_goods_route.addItems(list_yes_no)

        self.comboBox_general_info_road_school_bus_route = qtw.QComboBox()
        self.comboBox_general_info_road_school_bus_route.addItems(list_yes_no)

        self.comboBox_general_info_road_seasonal_volume_fluctuations = qtw.QComboBox()
        self.comboBox_general_info_road_seasonal_volume_fluctuations.addItems(list_yes_no)

        self.comboBox_general_info_road_sidewalks = qtw.QComboBox()
        self.comboBox_general_info_road_sidewalks.addItems(list_yes_no)

        #Group Labels
        self.label_general_info_rail_no_tracks_total = qtw.QLabel('No Value')
        self.label_general_info_rail_no_trains_per_day_total = qtw.QLabel('No Value')
        self.label_general_info_rail_railway_design_speed = qtw.QLabel('No Value')
        self.label_general_info_road_no_traffic_lanes_total = qtw.QLabel('No Value')

        # DESIGN CONSIDERATIONS (GCS SECTION 10)
        #Group TextEdits
        self.textEdit_design_observe_k_factor_other = qtw.QTextEdit()
        self.textEdit_design_comments = qtw.QTextEdit()

        #Group DoubleSpinBox
        self.doubleSpinBox_design_measure_adjacent_track_clearance_distance = qtw.QDoubleSpinBox()
        self.doubleSpinBox_design_measure_adjacent_track_clearance_distance.setRange(0, 999999)

        self.doubleSpinBox_design_measure_adjacent_track_separation_distance = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_design_measure_adjacent_track_separation_distance.setRange(0, 999999)

        self.doubleSpinBox_design_measure_clearance_distance_pedestrian = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian.setRange(0, 999999)

        self.doubleSpinBox_design_measure_clearance_distance_pedestrian_gate_arm_stop = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian.setRange(0, 999999)

        self.doubleSpinBox_design_measure_clearance_distance_vehicle = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_design_measure_clearance_distance_vehicle.setRange(0, 50)

        self.doubleSpinBox_design_road_max_approach_grade_within_s = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_design_road_max_approach_grade_within_s.setRange(-999999, 999999)        

        #Group ComboBoxes
        self.comboBox_design_observe_k_factor_road_surface_condition = qtw.QComboBox()
        self.comboBox_design_observe_k_factor_road_surface_condition.addItems(list_yes_no)
		
        self.comboBox_design_observe_k_factor_crossing_surface_condition = qtw.QComboBox()		
        self.comboBox_design_observe_k_factor_crossing_surface_condition.addItems(list_yes_no)

        self.comboBox_design_observe_k_factor_superelevation = qtw.QComboBox()
        self.comboBox_design_observe_k_factor_superelevation.addItems(list_yes_no)

        self.comboBox_design_observe_k_factor_crossing_nearby_intersection = qtw.QComboBox()
        self.comboBox_design_observe_k_factor_crossing_nearby_intersection.addItems(list_yes_no)
        
        self.comboBox_design_observe_k_factor_vehicle_restrictions = qtw.QComboBox()
        self.comboBox_design_observe_k_factor_vehicle_restrictions.addItems(list_yes_no)

        self.comboBox_design_observe_k_factor_pavement_marking_condition = qtw.QComboBox()
        self.comboBox_design_observe_k_factor_pavement_marking_condition.addItems(list_yes_no)
        
        self.comboBox_design_observe_field_acceleration_times_exceed_td = qtw.QComboBox()
        self.comboBox_design_observe_field_acceleration_times_exceed_td.addItems(list_yes_no)

        self.comboBox_design_road_design_vehicle_type = qtw.QComboBox()
        self.comboBox_design_road_design_vehicle_type.addItems(list_design_road_design_vehicle_type)

        #Group Labels
        self.label_design_calculate_adjacent_track_clearance_time = qtw.QLabel('No Value')
        self.label_design_calculate_clearance_time_pedestrian_design_check = qtw.QLabel('No Value')
        self.label_design_calculate_clearance_time_vehicle_design_check = qtw.QLabel('No Value')
        self.label_design_calculate_gate_arm_clearance_time_pedestrian = qtw.QLabel('No Value')
        self.label_design_calculate_gate_arm_clearance_time_vehicle_ssd = qtw.QLabel('No Value')
        self.label_design_calculate_gate_arm_clearance_time_vehicle_stop = qtw.QLabel('No Value')
        self.label_design_calculate_gate_arm_clearance_time_vehicle_recommended = qtw.QLabel('No Value')
        self.label_design_calculate_vehicle_departure_time = qtw.QLabel('No Value')
        self.label_design_calculate_vehicle_departure_time_grade_adjusted = qtw.QLabel('No Value')
        self.label_design_calculate_vehicle_departure_time_gate_arm_clearance = qtw.QLabel('No Value')
        self.label_design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted = qtw.QLabel('No Value')

        self.label_design_calculate_vehicle_travel_distance = qtw.QLabel('No Value')
        self.label_design_input_reaction_time = qtw.QLabel()
        self.label_design_input_reaction_time.setNum(2)
        self.label_design_lookup_design_vehicle_class = qtw.QLabel('No Value')
        self.label_design_lookup_design_vehicle_length = qtw.QLabel('No Value')
        self.label_design_lookup_grade_adjustment_factor = qtw.QLabel('No Value')
        self.label_design_measure_clearance_distance_gate_arm_ssd = qtw.QLabel('No Value')
        self.label_design_measure_clearance_distance_gate_arm_stop = qtw.QLabel('No Value')

        # LOCATION OF GRADE CROSSING (GCS SECTION 11)
        #Group TextEdits
        self.textEdit_location_of_grade_crossing_comments = qtw.QTextEdit()

        #Group DoubleSpinBox
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_other_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_other_n_or_e_approach.setRange(0, 999999)

        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_other_s_of_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_other_s_of_w_approach.setRange(0, 999999)

        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach.setRange(0, 999999)
        
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach.setRange(0, 999999)
        
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach.setRange(0, 999999)
        
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach.setRange(0, 999999)

        #group ComboBoxes
        self.comboBox_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk = qtw.QComboBox()
        self.comboBox_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk.addItems(list_yes_no)

        self.comboBox_location_of_grade_crossing_queue_condition = qtw.QComboBox()
        self.comboBox_location_of_grade_crossing_queue_condition.addItems(list_yes_no)

        self.comboBox_location_of_grade_crossing_visibility_of_warning_lights = qtw.QComboBox()
        self.comboBox_location_of_grade_crossing_visibility_of_warning_lights.addItems(list_yes_no)
        
        # GRADE CROSSING SURFACE (GCS SECTION 5)
        #Group TextEdits
        self.textEdit_grade_crossing_surface_comments = qtw.QTextEdit()

        #Group DoubleSpinBox
        self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach.setRange(0, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_extension_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach.setRange(0, 999999)

        self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_width = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_width.setRange(0, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_n_or_e_approach.setRange(-999999, 999999)

        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_s_or_w_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_n_or_e_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_s_or_w_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_elevation_top_of_rail_above_road_surface = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_elevation_top_of_rail_above_road_surface.setRange(-999999, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_elevation_top_of_rail_below_road_surface = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_elevation_top_of_rail_below_road_surface.setRange(-999999, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_flangeway_depth = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_flangeway_depth.setRange(-999999, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_flangeway_width = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_flangeway_width.setRange(-999999, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_median_width = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_median_width.setRange(0, 999999)

        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_shoulder_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_shoulder_n_or_e_approach.setRange(0, 999999)

        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_shoulder_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_shoulder_s_or_w_approach.setRange(0, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_travel_lanes_width_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_travel_lanes_width_n_or_e_approach.setRange(0, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_travel_lanes_width_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_travel_lanes_width_s_or_w_approach.setRange(0, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_side_grinding_depth = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_side_grinding_depth.setRange(-999999, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_side_grinding_width = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_side_grinding_width.setRange(-999999, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_extension_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_extension_n_or_e_approach.setRange(0, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_extension_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_extension_s_or_w_approach.setRange(0, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_width_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_width_n_or_e_approach.setRange(0, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_width_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_width_s_or_w_approach.setRange(0, 999999)

        #Group ComboBoxes
        self.comboBox_grade_crossing_surface_observe_crossing_smoothness = qtw.QComboBox()
        self.comboBox_grade_crossing_surface_observe_crossing_smoothness.addItems(list_yes_no)

        self.comboBox_grade_crossing_surface_observe_crossing_surface_condition = qtw.QComboBox()
        self.comboBox_grade_crossing_surface_observe_crossing_smoothness.addItems(list_condition)

        self.comboBox_grade_crossing_surface_observe_material = qtw.QComboBox()
        self.comboBox_grade_crossing_surface_observe_material.addItems(list_grade_crossing_surface_observe_material)

        self.comboBox_grade_crossing_surface_observe_road_approach_surface_condition = qtw.QComboBox()
        self.comboBox_grade_crossing_surface_observe_road_approach_surface_condition.addItems(list_condition)

        self.comboBox_grade_crossing_surface_observe_road_approach_surface_type = qtw.QComboBox()
        self.comboBox_grade_crossing_surface_observe_road_approach_surface_type.addItems(list_grade_crossing_surface_observe_road_approach_surface_type)

        # ROAD GEOMETRY (GCS SECTION 6)
        #Group TextEdits 
        self.textEdit_road_geometry_comments = qtw.QTextEdit()

        #Group SpinBox
        self.spinBox_road_geometry_road_crossing_angle = qtw.QSpinBox() 

        #Group DoubleSpinBox
        self.doubleSpinBox_road_geometry_measure_railway_cross_slope = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_measure_railway_cross_slope.setRange(-999999, 999999)

        self.doubleSpinBox_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_n_or_e_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_s_or_w_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_n_or_e_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_s_or_w_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_road_geometry_rail_superelevation_rate = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_rail_superelevation_rate.setRange(-999999, 999999)
        
        self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.setRange(-999999, 999999)

        #Group ComboBoxes
        self.comboBox_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach = qtw.QComboBox()
        self.comboBox_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach = qtw.QComboBox()
        self.comboBox_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach.addItems(list_yes_no)

        self.comboBox_road_geometry_observe_low_bed_truck_condition = qtw.QComboBox()
        self.comboBox_road_geometry_observe_low_bed_truck_condition.addItems(list_yes_no)

        self.comboBox_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach = qtw.QComboBox()
        self.comboBox_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach = qtw.QComboBox()
        self.comboBox_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach.addItems(list_yes_no)
       
        self.comboBox_road_geometry_rail_superelevation = qtw.QComboBox() 
        self.comboBox_road_geometry_rail_superelevation.addItems(list_yes_no)

        #Group Labels
        self.label_road_geometry_lookup_gradient_difference = qtw.QLabel('No Value')
        #TBD self.label_road_geometry_observe_gradient_difference_n_or_e_approach = qtw.QLabel('No Value')
        #TBD self.label_road_geometry_observe_gradient_difference_s_or_w_approach = qtw.QLabel('No Value')
        
        # SIGHTLINES (GCS SECTION 7)
        #Group TextEdits
        self.textEdit_sightlines_comments = qtw.QTextEdit()
        
        #Group DoubleSpinBox
        self.doubleSpinBox_sightlines_measure_dssd_actual_n_or_e_approach_left = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dssd_actual_n_or_e_approach_left.setRange(0, 999999)

        self.doubleSpinBox_sightlines_measure_dssd_actual_n_or_e_approach_right = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dssd_actual_n_or_e_approach_right.setRange(0, 999999)

        self.doubleSpinBox_sightlines_measure_dssd_actual_s_or_w_approach_left = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dssd_actual_s_or_w_approach_left.setRange(0, 999999)

        self.doubleSpinBox_sightlines_measure_dssd_actual_s_or_w_approach_right = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dssd_actual_s_or_w_approach_right.setRange(0, 999999)

        self.doubleSpinBox_sightlines_measure_dstopped_actual_n_or_e_approach_driver_left = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dstopped_actual_n_or_e_approach_driver_left.setRange(0, 999999)

        self.doubleSpinBox_sightlines_measure_dstopped_actual_n_or_e_approach_driver_right = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dstopped_actual_n_or_e_approach_driver_right.setRange(0, 999999)

        self.doubleSpinBox_sightlines_measure_dstopped_actual_s_or_w_approach_driver_left = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dstopped_actual_s_or_w_approach_driver_left.setRange(0, 999999)

        self.doubleSpinBox_sightlines_measure_dstopped_actual_s_or_w_approach_driver_right = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dstopped_actual_s_or_w_approach_driver_right.setRange(0, 999999)

        self.doubleSpinBox_sightlines_measure_ssd_actual_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_ssd_actual_n_or_e_approach.setRange(0, 999999)

        self.doubleSpinBox_sightlines_measure_ssd_actual_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_ssd_actual_s_or_w_approach.setRange(0, 999999)

        #Group ComboBoxes
        self.comboBox_sightlines_observe_sightline_obstructions = qtw.QComboBox()
        self.comboBox_sightlines_observe_sightline_obstructions.addItems(list_yes_no)

        #Group Labels
        self.label_sightlines_calculate_dssd_vehicle_min_ft = qtw.QLabel('No Value')
        self.label_sightlines_calculate_dssd_vehicle_min_m = qtw.QLabel('No Value')
        self.label_sightlines_calculate_dstopped_pedestrian_min_ft = qtw.QLabel('No Value')
        self.label_sightlines_calculate_dstopped_pedestrian_min_m = qtw.QLabel('No Value')
        self.label_sightlines_calculate_dstopped_vehicle_min_ft = qtw.QLabel('No Value')
        self.label_sightlines_calculate_dstopped_vehicle_min_m = qtw.QLabel('No Value')
        self.label_sightlines_lookup_existing_active_crossing = qtw.QLabel('No Value')
        self.label_sightlines_lookup_existing_active_crossing_with_gates = qtw.QLabel('No Value')
        self.label_sightlines_lookup_ssd_minimum_n_or_e_approach = qtw.QLabel('No Value')
        self.label_sightlines_lookup_ssd_minimum_s_or_w_approach = qtw.QLabel('No Value')

        # SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)
        #Group TextEdits
        #DELETE self.textEdit_signs_and_markings_advisory_speed_comments = pass
        #DELETE self.textEdit_signs_and_markings_comments = pass
        #DELETE self.textEdit_signs_and_markings_emergency_notification_comments = pass
        #DELETE self.textEdit_signs_and_markings_number_of_tracks_comments = pass
        #DELETE self.textEdit_signs_and_markings_railway_crossing_ahead_comments = pass
        #DELETE self.textEdit_signs_and_markings_railway_crossing_comments = pass
        #DELETE self.textEdit_signs_and_markings_stop_comments = pass
        #DELETE self.textEdit_signs_and_markings_stop_sign_ahead_comments = pass

        #Group DoubleSpinBox
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_rail.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_road.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_height.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_rail.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_road.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_height.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_height.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_location_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_location_from_rail.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_location_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_location_from_road.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_height.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_location_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_location_from_rail.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_location_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_location_from_road.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_height.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_rail.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_road.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_height.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_rail.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_road.setRange(0, 999999)
        
        #Group ComboBoxes
        self.comboBox_signs_and_markings_advisory_speed_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_advisory_speed_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20 = qtw.QComboBox()
        self.comboBox_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_advisory_speed_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_advisory_speed_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20 = qtw.QComboBox()
        self.comboBox_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_dividing_lines_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_dividing_lines_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_condition = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_condition.addItems(list_condition)

        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_legible = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_legible.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_orientation = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_orientation.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_condition = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_condition.addItems(list_condition)

        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_legible = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_legible.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_orientation = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_orientation.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b = qtw.QComboBox()
        self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c = qtw.QComboBox()
        self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b = qtw.QComboBox()
        self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c = qtw.QComboBox()
        self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_per_mutcd = qtw.QComboBox()
        self.comboBox_signs_and_markings_per_mutcd.addItems(list_yes_no)

        self.comboBox_signs_and_markings_posted_speed_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_posted_speed_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_posted_speed_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_posted_speed_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a.addItems(list_yes_no)

        self.comboBox_signs_and_markings_railway_crossing_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a.addItems(list_yes_no)

        self.comboBox_signs_and_markings_railway_crossing_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_sidewalks_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_sidewalks_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_stop_n_or_e_approach_per_fig_8_4 = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_n_or_e_approach_per_fig_8_4.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_stop_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_stop_n_or_e_approach_same_post = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_n_or_e_approach_same_post.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_stop_s_or_w_approach_per_fig_8_4 = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_s_or_w_approach_per_fig_8_4.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_stop_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_stop_s_or_w_approach_same_post = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_s_or_w_approach_same_post.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_present.addItems(list_yes_no)

        # GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
        #Group TextEdits
        self.textEdit_gcws_warrants_comments = qtw.QTextEdit()
        
        # Group Labels
        self.label_gcws_warrant_private_9_3 = qtw.QLabel('No Value')
        self.label_gcws_warrant_private_9_3_1 = qtw.QLabel('No Value')
        self.label_gcws_warrant_private_9_3_2_a = qtw.QLabel('No Value')
        self.label_gcws_warrant_private_9_3_2_b = qtw.QLabel('No Value')
        self.label_gcws_warrant_private_9_3_2_c = qtw.QLabel('No Value')
        self.label_gcws_warrant_public_9_1 = qtw.QLabel('No Value')
        self.label_gcws_warrant_public_9_1_a = qtw.QLabel('No Value')
        self.label_gcws_warrant_public_9_1_b = qtw.QLabel('No Value')
        self.label_gcws_warrant_public_9_1_c = qtw.QLabel('No Value')
        self.label_gcws_warrant_public_9_1_d_i = qtw.QLabel('No Value')
        self.label_gcws_warrant_public_9_1_d_ii = qtw.QLabel('No Value')
        self.label_gcws_warrant_public_9_1_d_iii = qtw.QLabel('No Value')
        self.label_gcws_warrant_sidewalk_9_5 = qtw.QLabel('No Value')
        self.label_gates_gcws_warrant_private_9_4_1_a = qtw.QLabel('No Value')
        self.label_gates_gcws_warrant_private_9_4_1_b = qtw.QLabel('No Value')
        self.label_gates_gcws_warrant_private_9_4_1_c = qtw.QLabel('No Value')
        self.label_gates_gcws_warrant_public_9_2_1_a = qtw.QLabel('No Value')
        self.label_gates_gcws_warrant_public_9_2_1_b = qtw.QLabel('No Value')
        self.label_gates_gcws_warrant_public_9_2_1_c = qtw.QLabel('No Value')
        self.label_gates_gcws_warrant_public_9_2_1_d = qtw.QLabel('No Value')
        self.label_gates_gcws_warrant_public_9_2_1_e = qtw.QLabel('No Value')
        self.label_gates_gcws_warrant_sidewalk_9_6 = qtw.QLabel('No Value')

        # GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
        #Group TextEdits
        self.textEdit_gcws_comments = qtw.QTextEdit()
        
        #Group SpinBox
        self.spinBox_gcws_rail_design_warning_time_preemption = qtw.QSpinBox()
        self.spinBox_gcws_rail_design_warning_time_preemption.setRange(0, 999999)
        
        #Group DoubleSpinBox
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_from_rail.setRange(0, 999999)
        
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_from_road.setRange(0, 999999)
        
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_top_of_foundation = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_top_of_foundation.setRange(0, 999999)
        
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_slope_from_foundation = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_slope_from_foundation.setRange(0, 999999)
        
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_from_rail.setRange(0, 999999)
        
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_from_road.setRange(0, 999999)
        
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_top_of_foundation = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_top_of_foundation.setRange(0, 999999)
        
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_slope_from_foundation = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_slope_from_foundation.setRange(0, 999999)
        
        self.doubleSpinBox_gcws_rail_crossing_warning_time_actual = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gcws_rail_crossing_warning_time_actual.setRange(0, 999999)
        
        #Group ComboBox
        self.comboBox_gcws_observe_bell_if_sidewalk = qtw.QComboBox()
        self.comboBox_gcws_observe_bell_if_sidewalk.addItems(list_yes_no)

        self.comboBox_gcws_observe_bells_condition = qtw.QComboBox()
        self.comboBox_gcws_observe_bells_condition.addItems(list_condition)

        self.comboBox_gcws_observe_bells_n_or_e_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_bells_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_bells_s_or_w_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_bells_s_or_w_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_cantilever_lights_condition = qtw.QComboBox()
        self.comboBox_gcws_observe_cantilever_lights_condition.addItems(list_condition)

        self.comboBox_gcws_observe_cantilever_lights_n_or_e_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_cantilever_lights_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_cantilever_lights_s_or_w_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_cantilever_lights_s_or_w_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_gates_condition = qtw.QComboBox()
        self.comboBox_gcws_observe_gates_condition.addItems(list_condition)

        self.comboBox_gcws_observe_gates_n_or_e_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_gates_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_gates_s_or_w_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_gates_s_or_w_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_gcws_limited_use_with_walk_light_assembly = qtw.QComboBox()
        self.comboBox_gcws_observe_gcws_limited_use_with_walk_light_assembly.addItems(list_yes_no_na)

        self.comboBox_gcws_observe_gcws_limited_use_without_walk_light_assembly = qtw.QComboBox()
        self.comboBox_gcws_observe_gcws_limited_use_without_walk_light_assembly.addItems(list_yes_no_na)

        self.comboBox_gcws_observe_light_units_condition = qtw.QComboBox()
        self.comboBox_gcws_observe_light_units_condition.addItems(list_condition)

        self.comboBox_gcws_observe_light_units_n_or_e_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_light_units_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_light_units_s_or_w_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_light_units_s_or_w_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_warning_time_consistency = qtw.QComboBox()
        self.comboBox_gcws_observe_warning_time_consistency.addItems(list_yes_no_na)
        
        self.comboBox_gcws_observe_warning_time_consistency_reduced_speed = qtw.QComboBox()
        self.comboBox_gcws_observe_warning_time_consistency_reduced_speed.addItems(list_yes_no_na)

        self.comboBox_gcws_rail_cut_out_circuit_requirements = qtw.QComboBox()
        self.comboBox_gcws_rail_cut_out_circuit_requirements.addItems(list_yes_no_na)

        self.comboBox_gcws_rail_directional_stick_circuit_requirements = qtw.QComboBox()
        self.comboBox_gcws_rail_directional_stick_circuit_requirements.addItems(list_yes_no_na)

        self.comboBox_gcws_rail_self_diagnostic = qtw.QComboBox()
        self.comboBox_gcws_rail_self_diagnostic.addItems(list_yes_no_na)

        #Group Labels
        self.label_gcws_rail_design_approach_warning_time = qtw.QLabel('No Value')
        self.label_gcws_rail_design_warning_time_ssd = qtw.QLabel('No Value')
        self.label_gcws_rail_design_warning_time_adjacent_crossing = qtw.QLabel('No Value')
        self.label_gcws_rail_design_warning_time_clearance_distance = qtw.QLabel('No Value')
        self.label_gcws_rail_design_warning_time_departure_time_pedestrian = qtw.QLabel('No Value')
        self.label_gcws_rail_design_warning_time_departure_time_vehicle = qtw.QLabel('No Value')
        self.label_gcws_rail_design_warning_time_gate_arm_clearance = qtw.QLabel('No Value')
        self.label_gcws_rail_design_warning_time_ssd = qtw.QLabel('No Value')

        # FLASHING LIGHT UNITS (GCS SECTION 13 & 14)
        #Group TextEdits
        self.textEdit_light_units_comments = qtw.QTextEdit()

        #Group DoubleSpinBox
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_distance_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_distance_from_rail.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_distance_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_distance_from_road.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_dl = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_dl.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_dr = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_dr.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_height.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_distance_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_distance_from_rail.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_distance_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_distance_from_road.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_dl = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_dl.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_dr = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_dr.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_height.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_n_or_e_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_n_or_e_approach_height.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_s_or_w_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_s_or_w_approach_height.setRange(0, 999999)
        
        #Group ComboBoxes
        self.comboBox_light_units_observe_cantilevers_per_fig_12_3 = qtw.QComboBox()
        self.comboBox_light_units_observe_cantilevers_per_fig_12_3.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_per_fig_12_1 = qtw.QComboBox()
        self.comboBox_light_units_observe_per_fig_12_1.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_sidewalks_n_or_e_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_sidewalks_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_sidewalks_s_or_w_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_sidewalks_s_or_w_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_supplemental_lights_n_or_e_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_supplemental_lights_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_supplemental_lights_s_or_w_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_supplemental_lights_s_or_w_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_visibility_back_lights_n_or_e_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_visibility_back_lights_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_visibility_back_lights_s_or_w_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_visibility_back_lights_s_or_w_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_visibility_front_lights_n_or_e_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_visibility_front_lights_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_visibility_front_lights_s_or_w_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_visibility_front_lights_s_or_w_approach.addItems(list_yes_no_na)

        # GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
        #Group TextEdits
        self.textEdit_gates_gcws_comments = qtw.QTextEdit()

        #Group DoubleSpinBox
        self.doubleSpinBox_gates_gcws_measure_gate_ascent_time = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gates_gcws_measure_gate_ascent_time.setRange(0, 999999)
        
        self.doubleSpinBox_gates_gcws_measure_gate_descent_time = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gates_gcws_measure_gate_descent_time.setRange(0, 999999)
        
        self.doubleSpinBox_gates_gcws_rail_gate_arm_delay_time_design = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gates_gcws_rail_gate_arm_delay_time_design.setRange(0, 999999)
        
        self.doubleSpinBox_gates_gcws_rail_gate_arm_descent_time_design = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gates_gcws_rail_gate_arm_descent_time_design.setRange(0, 999999)
        
        self.doubleSpinBox_gates_gcws_rail_inner_gate_arm_delay_time_design = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gates_gcws_rail_inner_gate_arm_delay_time_design.setRange(0, 999999)
        
        #Group DoubleSpinBox
        self.doubleSpinBox_gates_gcws_measure_distance_between_gate_end_and_road_cl_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gates_gcws_measure_distance_between_gate_end_and_road_cl_s_or_w_approach = qtw.QDoubleSpinBox() 

        #Group Labels
        self.label_gates_gcws_calculate_inner_gate_arm_delay_time_recommended = qtw.QLabel('No Value')

        #Group ComboBoxes
        self.comboBox_gates_gcws_observe_gate_arm_rest = qtw.QComboBox()
        self.comboBox_gates_gcws_observe_gate_arm_rest.addItems(list_yes_no_na)

        self.comboBox_gates_gcws_observe_gate_ascent_time = qtw.QComboBox()
        self.comboBox_gates_gcws_observe_gate_ascent_time.addItems(list_yes_no_na)

        self.comboBox_gates_gcws_observe_gate_descent_time = qtw.QComboBox()
        self.comboBox_gates_gcws_observe_gate_descent_time.addItems(list_yes_no_na)

        self.comboBox_gates_gcws_observe_gate_strips_n_or_e_approach = qtw.QComboBox()
        self.comboBox_gates_gcws_observe_gate_strips_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_gates_gcws_observe_gate_strips_s_or_w_approach = qtw.QComboBox()
        self.comboBox_gates_gcws_observe_gate_strips_s_or_w_approach.addItems(list_yes_no_na)

        self.comboBox_gates_gcws_observe_per_fig_12_2 = qtw.QComboBox()
        self.comboBox_gates_gcws_observe_per_fig_12_2.addItems(list_yes_no_na)

        # PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
        #Group Text Edits
        self.textEdit_aawd_comments = qtw.QTextEdit()

        #Group DoubleSpinBox
        self.doubleSpinBox_aawd_measure_distance_sign_and_stop_n_or_e_approach_actual = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_aawd_measure_distance_sign_and_stop_n_or_e_approach_actual.setRange(0, 999999)

        self.doubleSpinBox_aawd_measure_distance_sign_and_stop_s_or_w_approach_actual = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_aawd_measure_distance_sign_and_stop_s_or_w_approach_actual.setRange(0, 999999)

        #Group ComboBoxes
        self.comboBox_aawd_observe_present_n_or_e_approach = qtw.QComboBox()
        self.comboBox_aawd_observe_present_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_aawd_observe_present_s_or_w_approach = qtw.QComboBox()
        self.comboBox_aawd_observe_present_s_or_w_approach.addItems(list_yes_no)

        self.comboBox_aawd_road_aawd_sufficient_activation_time_n_or_e_approach = qtw.QComboBox()
        self.comboBox_aawd_road_aawd_sufficient_activation_time_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_aawd_road_aawd_sufficient_activation_time_s_or_w_approach = qtw.QComboBox()
        self.comboBox_aawd_road_aawd_sufficient_activation_time_s_or_w_approach.addItems(list_yes_no_na)

        self.comboBox_aawd_warrant_gcr_observe_environmental_condition = qtw.QComboBox()
        self.comboBox_aawd_road_aawd_sufficient_activation_time_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_aawd_warrant_gcr_observe_sightline_obstruction = qtw.QComboBox()
        self.comboBox_aawd_road_aawd_sufficient_activation_time_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_aawd_warrant_mutcd_lookup_significant_road_downgrade = qtw.QComboBox()
        self.comboBox_aawd_road_aawd_sufficient_activation_time_n_or_e_approach.addItems(list_yes_no_na)

        #Group Labels
        self.label_aawd_calculate_advance_activation_time_design_n_or_e_approach = qtw.QLabel('No Value')
        self.label_aawd_calculate_advance_activation_time_design_s_or_w_approach = qtw.QLabel('No Value')
        self.label_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended = qtw.QLabel('No Value')
        self.label_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended = qtw.QLabel('No Value')
        self.label_aawd_warrant_gcr_lookup_road_classification = qtw.QLabel('No Value')
        self.label_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr = qtw.QLabel('No Value')
        
        # INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
        #Group TextEdits
        self.textEdit_preemption_of_traffic_signals_comments = qtw.QTextEdit()
    
        #Group SpinBox
        self.spinBox_preemption_of_traffic_signals_road_preemption_warning_time_actual = qtw.QSpinBox() 
        self.spinBox_preemption_of_traffic_signals_road_preemption_warning_time_design = qtw.QSpinBox() 

        #Group CombBoxes
        self.comboBox_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles.addItems(list_yes_no)

        self.comboBox_preemption_of_traffic_signals_observe_known_queuing_issues = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_known_queuing_issues.addItems(list_yes_no)

        self.comboBox_preemption_of_traffic_signals_observe_pedestrian_accommodation = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_pedestrian_accommodation.addItems(list_yes_no_na)

        self.comboBox_preemption_of_traffic_signals_observe_queuing_condition = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_queuing_condition.addItems(list_yes_no)

        self.comboBox_preemption_of_traffic_signals_observe_supplemental_signage = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_supplemental_signage.addItems(list_yes_no_na)

        self.comboBox_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate.addItems(list_yes_no_na)

        self.comboBox_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals.addItems(list_yes_no_na)

        self.comboBox_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type.addItems(list_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type)

        #Group DatePicker
        #TODO self.label_preemption_of_traffic_signals_road_date_Last_preemption_check = pass

        #Group Labels
        self.label_preemption_of_traffic_signals_lookup_proximity_condition = qtw.QLabel('No Value')
        self.label_preemption_of_traffic_signals_lookup_required = qtw.QLabel('No Value')

        # WHISTLE CESSATION (GCS SECTION Appendix D)
        #Group TextEdits
        self.textEdit_areas_without_train_whistling_comments = qtw.QTextEdit()

        #Group ComboBoxes
        self.comboBox_areas_without_train_whistling_lookup_gcs_12_to_16 = qtw.QComboBox()
        self.comboBox_areas_without_train_whistling_lookup_gcs_12_to_16.addItems(list_yes_no_na)

        self.comboBox_areas_without_train_whistling_observe_for_stop_and_proceed = qtw.QComboBox()
        self.comboBox_areas_without_train_whistling_observe_for_stop_and_proceed.addItems(list_yes_no_na)

        self.comboBox_areas_without_train_whistling_observe_trespassing_area = qtw.QComboBox()
        self.comboBox_areas_without_train_whistling_observe_trespassing_area.addItems(list_yes_no)

        self.comboBox_areas_without_train_whistling_rail_anti_whistling_zone = qtw.QComboBox()
        self.comboBox_areas_without_train_whistling_rail_anti_whistling_zone.addItems(list_yes_no)

        self.comboBox_areas_without_train_whistling_rail_anti_whistling_zone_24_hrs = qtw.QComboBox()
        self.comboBox_areas_without_train_whistling_rail_anti_whistling_zone_24_hrs.addItems(list_yes_no)        

        #Group Labels
        self.label_areas_without_train_whistling_lookup_gcs_9_2 = qtw.QLabel('No Value')
        self.label_areas_without_train_whistling_requirements_lookup_table_d1_criteria = qtw.QLabel('No Value')
        self.label_areas_without_train_whistling_requirements_observe_table_D1 = qtw.QLabel('No Value')
        
        ##################
        # Layout Objects #
        ##################
        main_layout = qtw.QGridLayout()
        toolbox = qtw.QToolBox()
        self.setLayout(main_layout)
        main_layout.addWidget(toolbox, 0, 0)

        styleSheet = """
                        QToolBox::tab {
                            border: 1px solid #C4C4C3;
                            border-bottom-color: RGB(0, 0, 255);
                        }

                        QToolBox::tab:selected {
                            background-color: #f14040;
                            border-bottom-style: none;
                        }
                     """ 

        # QWidgets - Create a container widget
        container_inspection_details = qtw.QWidget(self)
        container_collision_history = qtw.QWidget(self)
        container_general_information = qtw.QWidget(self)
        container_design_considerations = qtw.QWidget(self)
        container_location_of_crossing = qtw.QWidget(self)
        container_crossing_surface = qtw.QWidget(self)
        container_road_geometry = qtw.QWidget(self)
        container_sightlines = qtw.QWidget(self)
        container_signs_and_pavement_markings = qtw.QWidget(self)
        container_gcws_warrants = qtw.QWidget(self)
        container_gcws = qtw.QWidget(self)
        container_gcws_lights = qtw.QWidget(self)
        container_gcws_gates = qtw.QWidget(self)
        container_aaws = qtw.QWidget(self)
        container_interconnection_traffic_signals = qtw.QWidget(self)
        container_whistle_cessation = qtw.QWidget(self)

        #QFormLayout - Create a form layout
        form_layout_inspection_details = qtw.QFormLayout()
        form_layout_collision_history = qtw.QFormLayout()
        form_layout_general_information = qtw.QFormLayout()
        form_layout_design_considerations = qtw.QFormLayout()
        form_layout_location_of_crossing = qtw.QFormLayout()
        form_layout_crossing_surface = qtw.QFormLayout()
        form_layout_road_geometry = qtw.QFormLayout()
        form_layout_sightlines = qtw.QFormLayout()
        form_layout_signs_and_pavement_markings = qtw.QFormLayout()
        form_layout_gcws_warrants = qtw.QFormLayout()
        form_layout_gcws = qtw.QFormLayout()
        form_layout_gcws_lights = qtw.QFormLayout()
        form_layout_gcws_gates = qtw.QFormLayout()
        form_layout_aaws = qtw.QFormLayout()
        form_layout_interconnection_traffic_signals = qtw.QFormLayout()
        form_layout_whistle_cessation = qtw.QFormLayout()

        #Set Form Layouts to Container Widgets
        container_inspection_details.setLayout(form_layout_inspection_details)        
        container_collision_history.setLayout(form_layout_collision_history)
        container_general_information.setLayout(form_layout_general_information)
        container_design_considerations.setLayout(form_layout_design_considerations)
        container_location_of_crossing.setLayout(form_layout_location_of_crossing)
        container_crossing_surface.setLayout(form_layout_crossing_surface)
        container_road_geometry.setLayout(form_layout_road_geometry)
        container_sightlines.setLayout(form_layout_sightlines)
        container_signs_and_pavement_markings.setLayout(form_layout_signs_and_pavement_markings)
        container_gcws_warrants.setLayout(form_layout_gcws_warrants)
        container_gcws.setLayout(form_layout_gcws)
        container_gcws_lights.setLayout(form_layout_gcws_lights)
        container_gcws_gates.setLayout(form_layout_gcws_gates)
        container_aaws.setLayout(form_layout_aaws)
        container_interconnection_traffic_signals.setLayout(form_layout_interconnection_traffic_signals)
        container_whistle_cessation.setLayout(form_layout_whistle_cessation)

        #Add Container Widgets to Toolbox
        toolbox.addItem(container_inspection_details, 'INSPECTION DETAILS')
        toolbox.addItem(container_collision_history, 'COLLISION HISTORY (5 YEAR PERIOD)')
        toolbox.addItem(container_general_information, 'GENERAL INFORMATION')
        toolbox.addItem(container_design_considerations, 'DESIGN CONSIDERATIONS (GCS SECTION 10)')
        toolbox.addItem(container_location_of_crossing, 'LOCATION OF GRADE CROSSING (GCS SECTION 11)')
        toolbox.addItem(container_crossing_surface, 'CROSSING SURFACE (GCS SECTION 5)')
        toolbox.addItem(container_road_geometry, 'ROAD GEOMETRY (GCS SECTION 6)')
        toolbox.addItem(container_sightlines, 'SIGHTLINES (GCS SECTION 7)')
        toolbox.addItem(container_signs_and_pavement_markings, 'SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)')
        toolbox.addItem(container_gcws_warrants, 'GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)')
        toolbox.addItem(container_gcws, 'GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)')
        toolbox.addItem(container_gcws_lights, 'FLASHING LIGHT UNITS (GCS SECTION 13 & 14)')
        toolbox.addItem(container_gcws_gates, 'GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)')
        toolbox.addItem(container_aaws, 'PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)')
        toolbox.addItem(container_interconnection_traffic_signals, 'INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)')
        toolbox.addItem(container_whistle_cessation, 'WHISTLE CESSATION (GCS SECTION Appendix D)')

        toolbox.setCurrentIndex(0)
        toolbox.setStyleSheet(styleSheet)
        
        # layout container widgets - INSPECTION DETAILS
        #TODO form_layout_inspection_details.addRow('Date of Assessment:', self.label_inspection_details_date_assessment)
        form_layout_inspection_details.addRow('Assessment Team Members & Affiliations:', self.textEdit_inspection_details_assessment_team)
        form_layout_inspection_details.addRow('Reason for Assessment:', self.comboBox_inspection_details_reason_for_assessment)
        form_layout_inspection_details.addRow('Railway Authority:', self.comboBox_inspection_details_railway_authority)
        form_layout_inspection_details.addRow('Crossing Location:', self.lineEdit_inspection_details_crossing_location)
        form_layout_inspection_details.addRow('Location Number:', self.lineEdit_inspection_details_location_number)
        form_layout_inspection_details.addRow('Subdivision Name:', self.comboBox_inspection_details_subdivision_name)
        form_layout_inspection_details.addRow('Subdivision Mile:', self.doubleSpinBox_inspection_details_subdivision_mile)
        form_layout_inspection_details.addRow('Spur Name:', self.lineEdit_inspection_details_spur_name)
        form_layout_inspection_details.addRow('Spur Mile:', self.doubleSpinBox_inspection_details_spur_mile)
        form_layout_inspection_details.addRow('Type of Crossing:', self.comboBox_inspection_details_grade_crossing_type)     
        form_layout_inspection_details.addRow('Type of Protection:', self.comboBox_inspection_details_gcws_type)
        form_layout_inspection_details.addRow('Track Type:', self.comboBox_inspection_details_track_type)
        form_layout_inspection_details.addRow('Road Authority:', self.comboBox_inspection_details_road_authority)
        form_layout_inspection_details.addRow('Municipality:', self.lineEdit_inspection_details_municipality)
        form_layout_inspection_details.addRow('Road Name:', self.lineEdit_inspection_details_road_name)   
        form_layout_inspection_details.addRow('Road Number:', self.lineEdit_inspection_details_road_number)
        form_layout_inspection_details.addRow('Province:', self.comboBox_inspection_details_province)     
        form_layout_inspection_details.addRow('Latitude:', self.doubleSpinBox_inspection_details_latitude)
        form_layout_inspection_details.addRow('Longitude:', self.doubleSpinBox_inspection_details_longitude)

        # layout container widgets - COLLISION HISTORY (5 YEAR PERIOD)
        form_layout_collision_history.addRow('Property Damage Collisions:', self.spinBox_collision_history_property_damage)
        form_layout_collision_history.addRow('Personal Injury Collisions:', self.spinBox_collision_history_personal_injury)
        form_layout_collision_history.addRow('Fatal Injury Collisions:', self.spinBox_collision_history_fatal_injury)
        form_layout_collision_history.addRow('Total Collisions in the last 5 year period:', self.label_collision_history_total_5_year_period)
        form_layout_collision_history.addRow('Number of Persons Injured:', self.spinBox_collision_history_fatalities)
        form_layout_collision_history.addRow('Number of Persons Killed:', self.spinBox_collision_history_personal_injuries)
        form_layout_collision_history.addRow('Details of Collisions:', self.textEdit_collision_history_comments)
        form_layout_collision_history.addRow('Risk Index (Initial), a Factor:', self.label_collision_history_risk_index_initial)
        form_layout_collision_history.addRow('Risk Index (Final), B Factor (T=5 years):', self.label_collision_history_risk_index_final)

        # layout container widgets - GENERAL INFORMATION
        form_layout_general_information.addRow(qtw.QLabel('Railway Speed'))
        form_layout_general_information.addRow('Maximum Freight Railway Operating Speed (mph):', self.spinBox_general_info_rail_max_railway_operating_speed_freight)
        form_layout_general_information.addRow('Maximum Passenger Railway Operating Speed (mph):', self.spinBox_general_info_rail_max_railway_operating_speed_passenger)
        form_layout_general_information.addRow('Railway Design Speed, VT (mph):', self.label_general_info_rail_railway_design_speed)
        form_layout_general_information.addRow(qtw.QLabel('Type and Number of Tracks'))
        form_layout_general_information.addRow('Main:', self.spinBox_general_info_rail_no_tracks_main)
        form_layout_general_information.addRow('Other:', self.spinBox_general_info_rail_no_tracks_other)
        form_layout_general_information.addRow('Total Number of Tracks:', self.label_general_info_rail_no_tracks_total)
        form_layout_general_information.addRow(qtw.QLabel('Average Daily Train Volume'))
        form_layout_general_information.addRow('Freight Trains/Day:', self.spinBox_general_info_rail_no_trains_per_day_freight)
        form_layout_general_information.addRow('Passenger Trains/Day:', self.spinBox_general_info_rail_no_trains_per_day_passengers)
        form_layout_general_information.addRow('Total Trains/Day:', self.label_general_info_rail_no_trains_per_day_total)
        form_layout_general_information.addRow('Train Switching within Crossing Approaches?:', self.comboBox_general_info_rail_train_switching)
        form_layout_general_information.addRow('Road Crossing Design Speed (km/hr):', self.spinBox_general_info_road_speed_design)
        form_layout_general_information.addRow('Road Posted Speed (km/hr):', self.spinBox_general_info_road_speed_posted)
        form_layout_general_information.addRow(qtw.QLabel('No. of Traffic Lanes Traversing Crossing'))
        form_layout_general_information.addRow('Northbound / Eastbound:', self.spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound)
        form_layout_general_information.addRow('Southbound / Westbound:', self.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound)
        form_layout_general_information.addRow('Bidirectional:', self.spinBox_general_info_road_no_traffic_lanes_bidirectional)
        form_layout_general_information.addRow('Total:', self.label_general_info_road_no_traffic_lanes_total)
        form_layout_general_information.addRow('Current Average Annual Daily Traffic, AADT:', self.spinBox_general_info_road_aadt_current)
        form_layout_general_information.addRow('Year of Count:', self.spinBox_general_info_road_aadt_year_current)
        form_layout_general_information.addRow('Forecasted Average Annual Daily Traffic, AADT:', self.spinBox_general_info_road_aadt_forecast)
        form_layout_general_information.addRow('Forecast Year:', self.spinBox_general_info_road_aadt_year_forecasted)
        form_layout_general_information.addRow('Pedestrian Volume per Day:', self.spinBox_general_info_road_pedestrians_per_day)
        form_layout_general_information.addRow('Cyclist Volume per Day:', self.spinBox_general_info_road_cyclist_per_day)
        form_layout_general_information.addRow('Other Special Road Users?:', self.lineEdit_general_info_road_other_users)
        form_layout_general_information.addRow('Volume', self.spinBox_general_info_road_other_users_daily_users)
        form_layout_general_information.addRow('High Seasonal Fluctuation in Volumes?:', self.comboBox_general_info_road_seasonal_volume_fluctuations)
        form_layout_general_information.addRow('Road Classification', self.comboBox_general_info_road_classification)
        form_layout_general_information.addRow('Does Grade Crossing Include sidewalk, Path, or Trail?:', self.comboBox_general_info_road_sidewalks)
        form_layout_general_information.addRow('Regular Use of Crossing by Persons with Assistive Devices?:', self.comboBox_general_info_road_assistive_pedestrian_devices)
        form_layout_general_information.addRow('Is Crossing on a School Bus Route?:', self.comboBox_general_info_road_school_bus_route)
        form_layout_general_information.addRow('Do Dangerous Goods Trucks Use this Roadway?:', self.comboBox_general_info_road_dangerous_goods_route)
        form_layout_general_information.addRow('Surrounding Land Use:', self.comboBox_general_info_observe_surrounding_land_use)
        form_layout_general_information.addRow('Any schools, retirement homes, etc. nearby?:', self.lineEdit_general_info_observe_special_buildings)        
        form_layout_general_information.addRow('Roadway Illumination?:', self.comboBox_general_info_observe_roadway_illumination)
        form_layout_general_information.addRow('Comments Regarding General Information:', self.textEdit_general_info_comments)

        # layout container widgets - DESIGN CONSIDERATIONS (GCS SECTION 10)
        form_layout_design_considerations.addRow('Design Vehicle Type:', self.comboBox_design_road_design_vehicle_type)
        form_layout_design_considerations.addRow('Design Vehicle Class:', self.label_design_lookup_design_vehicle_class)
        form_layout_design_considerations.addRow('Design Vehicle Length (m):', self.label_design_lookup_design_vehicle_length)
        form_layout_design_considerations.addRow('Clearance Distance - Vehicle, cd (m):', self.doubleSpinBox_design_measure_clearance_distance_vehicle)
        form_layout_design_considerations.addRow('Vehicle Travel Distance, S = L + cd (m):', self.label_design_calculate_vehicle_travel_distance)
        form_layout_design_considerations.addRow(qtw.QLabel('Clearance Time for Vehicles, TVeh (s)'))
        form_layout_design_considerations.addRow('Maximum Road Approach Grade within S (%):', self.doubleSpinBox_design_road_max_approach_grade_within_s)
        form_layout_design_considerations.addRow('Grade Adjustment Factor (G):', self.label_design_lookup_grade_adjustment_factor)
        form_layout_design_considerations.addRow('Departure Time - Vehicle (without Grade Adjustment Factor) (t):', self.label_design_calculate_vehicle_departure_time)
        form_layout_design_considerations.addRow('Departure Time - Vehicle (with Grade Adjustment Factor) (T = txG):', self.label_design_calculate_vehicle_departure_time_grade_adjusted)
        form_layout_design_considerations.addRow("Driver's Reaction Time (s):", self.label_design_input_reaction_time)
        form_layout_design_considerations.addRow('Clearance Time - Vehicle, Td = J + T:', self.label_design_calculate_clearance_time_vehicle_design_check)
        form_layout_design_considerations.addRow(qtw.QLabel('Clearance Time for Pedestrians, TPed (s)'))
        form_layout_design_considerations.addRow('Clearance Distance - Pedestrian, cd (m):', self.doubleSpinBox_design_measure_clearance_distance_pedestrian)
        form_layout_design_considerations.addRow('Clearance Time - Pedestrian, Td = J + T:', self.label_design_calculate_clearance_time_pedestrian_design_check)
        form_layout_design_considerations.addRow(qtw.QLabel('Adjacent Track Clearance Time'))
        form_layout_design_considerations.addRow('Separation Distance Between Adjacent Tracks (m):', self.doubleSpinBox_design_measure_adjacent_track_separation_distance)              
        form_layout_design_considerations.addRow('Adjacent Track Clearance Distance (m):', self.doubleSpinBox_design_measure_adjacent_track_clearance_distance)
        form_layout_design_considerations.addRow('Adjacent Track Clearance Time (s):', self.label_design_calculate_adjacent_track_clearance_time)
        form_layout_design_considerations.addRow(qtw.QLabel('Gate Arm Clearance Time for Vehicles, TG, Veh (s)'))
        form_layout_design_considerations.addRow(qtw.QLabel('Vehicle Gate Arm Clearance Time from SSD'))
        #form_layout_design_considerations.addRow('Vehicle Stopping Sight Distance', max(self.label_sightlines_lookup_ssd_minimum_n_or_e_approach,self.label_sightlines_lookup_ssd_minimum_s_or_w_approach))
        #form_layout_design_considerations.addRow('Road Design Speed', self.label_general_info_road_speed_design)
        form_layout_design_considerations.addRow('Gate Arm Clearance Time (from the SSD position) (TG,Veh SSD) (s):', self.label_design_calculate_gate_arm_clearance_time_vehicle_ssd)
        form_layout_design_considerations.addRow(qtw.QLabel('Vehicle Gate Arm Clearance Time from Stop'))
        form_layout_design_considerations.addRow('Vehicle Clearance Distance, Gate Arm from stop, cdG stop (m):', self.label_design_measure_clearance_distance_gate_arm_stop)
        form_layout_design_considerations.addRow('Vehicle Departure Time, Gate Arm Clearance (without Grade Adjustmenet Factor), t (s):', self.label_design_calculate_vehicle_departure_time_gate_arm_clearance)        
        form_layout_design_considerations.addRow('Vehicle Departure Time, Gate Arm Clearance (with Grade Adjustmenet Factor), T=(txG) (s):', self.label_design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted)
        form_layout_design_considerations.addRow('Gate Arm Clearance Time (from the Stop position) (TG,Veh Stop) (s):', self.label_design_calculate_gate_arm_clearance_time_vehicle_stop)
        form_layout_design_considerations.addRow('Gate Arm Clearance Time (Recommended) (TG, Veh) (s):', self.label_design_calculate_gate_arm_clearance_time_vehicle_recommended)
        form_layout_design_considerations.addRow(qtw.QLabel('Gate Arm Clearance Time for Stand-Alone Sidewalks, Paths or Trails, TG,Ped'))
        form_layout_design_considerations.addRow('Gate Arm Clearance Distance, Pedestrian (SPTcd)', self.doubleSpinBox_design_measure_clearance_distance_pedestrian_gate_arm_stop)
        form_layout_design_considerations.addRow('Pedestrian Gate Arm Clearance Time (TGPed)', self.label_design_calculate_gate_arm_clearance_time_pedestrian)
        form_layout_design_considerations.addRow(qtw.QLabel('Additional Time Required Due to Crossing Conditions, K (s)'))
        form_layout_design_considerations.addRow('Condition of the road surface:', self.comboBox_design_observe_k_factor_road_surface_condition)					
        form_layout_design_considerations.addRow('Condition of crossing surface:', self.comboBox_design_observe_k_factor_crossing_surface_condition)					
        form_layout_design_considerations.addRow('Super elevated track at the grade crossing:', self.comboBox_design_observe_k_factor_superelevation)				
        form_layout_design_considerations.addRow('An intersection on the departure side of the grade crossing where vehicles are required to stop, which reduces vehicle acceleration over the crossing:', self.comboBox_design_observe_k_factor_crossing_nearby_intersection)
        form_layout_design_considerations.addRow('Restrictions on the vehicle operator from shifting gears while passing over the grade crossing:', self.comboBox_design_observe_k_factor_vehicle_restrictions)
        form_layout_design_considerations.addRow('Non-standard placement of the stop line pavement markings:', self.comboBox_design_observe_k_factor_pavement_marking_condition)
        form_layout_design_considerations.addRow('Other (Describe situation):', self.textEdit_design_observe_k_factor_other)
        form_layout_design_considerations.addRow('Do Field Acceleration Times Exceed Td?:', self.comboBox_design_observe_field_acceleration_times_exceed_td)
        form_layout_design_considerations.addRow('Design Consideration Comments', self.textEdit_design_comments)

        # layout container widgets - LOCATION OF GRADE CROSSING (GCS SECTION 11)
        form_layout_location_of_crossing.addRow(qtw.QLabel('D (Intersection with Stop Sign)'))
        form_layout_location_of_crossing.addRow('N or E Road Approach (m):', self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach)
        form_layout_location_of_crossing.addRow('S or W Road Approach (m):', self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach)
        form_layout_location_of_crossing.addRow(qtw.QLabel('D (Signalized Intersection)'))
        form_layout_location_of_crossing.addRow('N or E Road Approach (m):', self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach)
        form_layout_location_of_crossing.addRow('S or W Road Approach (m):', self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach)
        form_layout_location_of_crossing.addRow(qtw.QLabel('D (Other Intersection / Driveway / Crosswalk)'))
        form_layout_location_of_crossing.addRow('N or E Road Approach (m):', self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_other_n_or_e_approach)
        form_layout_location_of_crossing.addRow('S or W Road Approach (m):', self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_other_s_of_w_approach)        
        form_layout_location_of_crossing.addRow('Is D insufficient such that road vehicles might queue onto the tracks?:', self.comboBox_location_of_grade_crossing_queue_condition)
        form_layout_location_of_crossing.addRow('Is D insufficient such that road vehicles turning from a side street might not see warning devices for the crossing?:', self.comboBox_location_of_grade_crossing_visibility_of_warning_lights)
        form_layout_location_of_crossing.addRow('Are there pedestrian crossings on either road approach that could cause vehicles to queue back to the tracks?:', self.comboBox_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk)
        form_layout_location_of_crossing.addRow('Location of Grade Crossing Comments:', self.textEdit_location_of_grade_crossing_comments)

        # layout container widgets - GRADE CROSSING SURFACE (GCS SECTION 5)
        form_layout_crossing_surface.addRow('Is the crossing smooth enough to allow road vehicles, pedestrians, cyclists, and other road users to cross at their normal speed without consequence? Comments below.', self.comboBox_grade_crossing_surface_observe_crossing_smoothness)
        form_layout_crossing_surface.addRow('Grade Crossing Surface Material', self.comboBox_grade_crossing_surface_observe_material)
        form_layout_crossing_surface.addRow('Grade Crossing Surface Condition', self.comboBox_grade_crossing_surface_observe_crossing_surface_condition)
        form_layout_crossing_surface.addRow('Road Approach Surface Type', self.comboBox_grade_crossing_surface_observe_road_approach_surface_type)
        form_layout_crossing_surface.addRow('Road Approach Surface Condition', self.comboBox_grade_crossing_surface_observe_road_approach_surface_condition)        
        form_layout_crossing_surface.addRow('Crossing Surface Width (m):', self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_width)
        form_layout_crossing_surface.addRow('Centre Lane/Median Width (m):', self.doubleSpinBox_grade_crossing_surface_measure_road_surface_median_width)
        form_layout_crossing_surface.addRow(qtw.QLabel('Travelled Way Width (m):'))
        form_layout_crossing_surface.addRow('N or E Road Approach:', self.doubleSpinBox_grade_crossing_surface_measure_road_surface_travel_lanes_width_n_or_e_approach)
        form_layout_crossing_surface.addRow('S or W Road Approach:', self.doubleSpinBox_grade_crossing_surface_measure_road_surface_travel_lanes_width_s_or_w_approach)
        form_layout_crossing_surface.addRow(qtw.QLabel('Paved Shoulder Width (m):'))
        form_layout_crossing_surface.addRow('N or E Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_road_surface_shoulder_n_or_e_approach)
        form_layout_crossing_surface.addRow('S or W Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_road_surface_shoulder_s_or_w_approach)
        form_layout_crossing_surface.addRow(qtw.QLabel('Surface Extension beyond Travel Lanes/Shoulder (m):'))
        form_layout_crossing_surface.addRow('N or E Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach)
        form_layout_crossing_surface.addRow('S or W Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_extension_s_or_w_approach)
        form_layout_crossing_surface.addRow(qtw.QLabel('Sidewalk / Path / Trail Width (m):'))
        form_layout_crossing_surface.addRow('N or E Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_width_n_or_e_approach)
        form_layout_crossing_surface.addRow('S or W Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_width_s_or_w_approach)
        form_layout_crossing_surface.addRow(qtw.QLabel('Surface Extension beyond Sidewalk / Path / Trail (m):'))
        form_layout_crossing_surface.addRow('N or E Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_extension_n_or_e_approach)
        form_layout_crossing_surface.addRow('S or W Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_extension_s_or_w_approach)
        form_layout_crossing_surface.addRow(qtw.QLabel('Distance Between Travel Lane / Shoulder and Sidewalk / Path / Trail (m):'))
        form_layout_crossing_surface.addRow('N or E Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_n_or_e_approach)
        form_layout_crossing_surface.addRow('S or W Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_s_or_w_approach)
        form_layout_crossing_surface.addRow(qtw.QLabel('Distance from path centreline to crossing warning device (m):'))
        form_layout_crossing_surface.addRow('N or E Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_n_or_e_approach)
        form_layout_crossing_surface.addRow('S or W Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_s_or_w_approach)
        form_layout_crossing_surface.addRow('Flangeway Depth (mm):', self.doubleSpinBox_grade_crossing_surface_measure_flangeway_depth)
        form_layout_crossing_surface.addRow('Flangeway Width (mm):', self.doubleSpinBox_grade_crossing_surface_measure_flangeway_width)
        form_layout_crossing_surface.addRow('Field Side Grinding Depth (mm):', self.doubleSpinBox_grade_crossing_surface_measure_side_grinding_depth)
        form_layout_crossing_surface.addRow('Field Side Grinding Width (mm):', self.doubleSpinBox_grade_crossing_surface_measure_side_grinding_width)
        form_layout_crossing_surface.addRow('Elevation of top of Rail Above Road Surface (mm):', self.doubleSpinBox_grade_crossing_surface_measure_elevation_top_of_rail_above_road_surface)
        form_layout_crossing_surface.addRow('Elevation of top of Rail Below Road Surface (mm):', self.doubleSpinBox_grade_crossing_surface_measure_elevation_top_of_rail_below_road_surface)
        form_layout_crossing_surface.addRow('Crossing Surface Comments:', self.textEdit_grade_crossing_surface_comments)

        # layout container widgets - ROAD GEOMETRY (GCS SECTION 6)
        form_layout_road_geometry.addRow(qtw.QLabel('Are the horizontal and vertical alignments smooth and continuous throughout SSD?'))
        form_layout_road_geometry.addRow('N or E Road Approach:', self.comboBox_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach)
        form_layout_road_geometry.addRow('S or W Road Approach:', self.comboBox_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach)
        form_layout_road_geometry.addRow(qtw.QLabel('Are the road lanes and shoulders at least the same width on the crossing as on the road approaches?'))
        form_layout_road_geometry.addRow('N or E Road Approach:', self.comboBox_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach)
        form_layout_road_geometry.addRow('S or W Road Approach:', self.comboBox_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach)
        form_layout_road_geometry.addRow(qtw.QLabel('Road Approach Grades (%):'))
        form_layout_road_geometry.addRow('Within 8m (N or E Road Approach):', self.doubleSpinBox_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach)
        form_layout_road_geometry.addRow('Within 8m (S or W Road Approach):', self.doubleSpinBox_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach)
        form_layout_road_geometry.addRow('Between 8m to 18m (N or E Road Approach):', self.doubleSpinBox_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_n_or_e_approach)
        form_layout_road_geometry.addRow('Between 8m to 18m (S or W Road Approach):', self.doubleSpinBox_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_s_or_w_approach)
        form_layout_road_geometry.addRow('Across SSD (N or E Road Approach):', self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach)
        form_layout_road_geometry.addRow('Across SSD (S or W Road Approach):', self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach)
        form_layout_road_geometry.addRow('Within 5m of Sidewalk/Path/Trail (N or E Road Approach):', self.doubleSpinBox_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_n_or_e_approach)
        form_layout_road_geometry.addRow('Within 5m of Sidewalk/Path/Trail (S or W Road Approach):', self.doubleSpinBox_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_s_or_w_approach)
        form_layout_road_geometry.addRow('Allowable difference between roadway gradient and railway cross-slope (%)', self.label_road_geometry_lookup_gradient_difference)
        form_layout_road_geometry.addRow('Railway Cross Slope (%):', self.doubleSpinBox_road_geometry_measure_railway_cross_slope)
        #TBD
        #form_layout_road_geometry.addRow(qtw.QLabel(
        #    'Is the difference between the road approach gradient and the railway cross slope, ' + 
        #    'or the railway gradient and the road approach cross slope, in accordance with the ' +
        #    'design standards of the Geometric Design Guide (Table 2.3.13.1)?'))
        #form_layout_road_geometry.addRow('N or E Road Approach:', self.label_road_geometry_observe_gradient_difference_n_or_e_approach)
        #form_layout_road_geometry.addRow('S or W Road Approach:', self.label_road_geometry_observe_gradient_difference_s_or_w_approach)
        form_layout_road_geometry.addRow('Are rail tracks super elevated?:', self.comboBox_road_geometry_rail_superelevation)
        form_layout_road_geometry.addRow('Rate of super-elevation (inch):', self.doubleSpinBox_road_geometry_rail_superelevation_rate)
        form_layout_road_geometry.addRow('Is there any evidence that "low-bed" trucks have difficulty negotiating the crossing? (i.e. might they bottom-out or get stuck?)', self.comboBox_road_geometry_observe_low_bed_truck_condition)
        form_layout_road_geometry.addRow('Grade Crossing Angle:', self.spinBox_road_geometry_road_crossing_angle)
        form_layout_road_geometry.addRow('Road Geometry Comments:', self.textEdit_road_geometry_comments)

        # layout container widgets - SIGHTLINES (GCS SECTION 7)
        form_layout_sightlines.addRow('Is crossing an "Existing Active Crossing", where exempted from DSSD and partial DSTOPPED requirements?', self.label_sightlines_lookup_existing_active_crossing)																	
        form_layout_sightlines.addRow('Is crossing and "Existing Active Crossing with Gates", where exempted from DSTOPPED requirements?', self.label_sightlines_lookup_existing_active_crossing_with_gates)																	
        form_layout_sightlines.addRow(qtw.QLabel("Stopping Sight Distance (SSD) Sightlines"))
        form_layout_sightlines.addRow('SSD Minimum (N or E Road Approach) (m):', self.label_sightlines_lookup_ssd_minimum_n_or_e_approach)
        form_layout_sightlines.addRow('SSD Minimum (S or W Road Approach) (m):', self.label_sightlines_lookup_ssd_minimum_s_or_w_approach)
        form_layout_sightlines.addRow('SSD Actual (N or E Road Approach) (m):', self.doubleSpinBox_sightlines_measure_ssd_actual_n_or_e_approach)
        form_layout_sightlines.addRow('SSD Actual (S or W Road Approach) (m):', self.doubleSpinBox_sightlines_measure_ssd_actual_s_or_w_approach)
        form_layout_sightlines.addRow(qtw.QLabel("DSSD Sightlines - For Users Approaching a Grade Crossing (See Fig 7-1(b))"))
        form_layout_sightlines.addRow('DSSD Minimum (ft):', self.label_sightlines_calculate_dssd_vehicle_min_ft)
        form_layout_sightlines.addRow('DSSD Minimum (m):', self.label_sightlines_calculate_dssd_vehicle_min_m)
        form_layout_sightlines.addRow("DSSD Actual (N or E Road Approach) (Driver's Left) (m):", self.doubleSpinBox_sightlines_measure_dssd_actual_n_or_e_approach_left)
        form_layout_sightlines.addRow("DSSD Actual (N or E Road Approach) (Driver's Right) (m):", self.doubleSpinBox_sightlines_measure_dssd_actual_n_or_e_approach_right)
        form_layout_sightlines.addRow("DSSD Actual (S or W Road Approach) (Driver's Left) (m):", self.doubleSpinBox_sightlines_measure_dssd_actual_s_or_w_approach_left)
        form_layout_sightlines.addRow("DSSD Actual (S or W Road Approach) (Driver's Right) (m):", self.doubleSpinBox_sightlines_measure_dssd_actual_s_or_w_approach_right)
        form_layout_sightlines.addRow(qtw.QLabel("Dstopped Sightlines - For Users Stopped at a Grade Crossing (See Fig 7-1(a))"))
        form_layout_sightlines.addRow('DStopped Minimum (Vehicle) (ft):', self.label_sightlines_calculate_dstopped_vehicle_min_ft)
        form_layout_sightlines.addRow('DStopped Minimum (Vehicle) (m):', self.label_sightlines_calculate_dstopped_vehicle_min_m)
        form_layout_sightlines.addRow('DStopped Minimum (Pedestiran) (ft):', self.label_sightlines_calculate_dstopped_pedestrian_min_ft)
        form_layout_sightlines.addRow('DStopped Minimum (Pedestrian) (m):', self.label_sightlines_calculate_dstopped_pedestrian_min_m)
        form_layout_sightlines.addRow("DStopped Actual (N or E Road Approach) (Driver's Left) (m):", self.doubleSpinBox_sightlines_measure_dstopped_actual_n_or_e_approach_driver_left)
        form_layout_sightlines.addRow("DStopped Actual (N or E Road Approach) (Driver's Right) (m):", self.doubleSpinBox_sightlines_measure_dstopped_actual_n_or_e_approach_driver_right)
        form_layout_sightlines.addRow("DStopped Actual (S or W Road Approach) (Driver's Left) (m):", self.doubleSpinBox_sightlines_measure_dstopped_actual_s_or_w_approach_driver_left)
        form_layout_sightlines.addRow("DStopped Actual (S or W Road Approach) (Driver's Right) (m):", self.doubleSpinBox_sightlines_measure_dstopped_actual_s_or_w_approach_driver_right)
        form_layout_sightlines.addRow("Are there any obstacles within the sight triangles that affect visibility?", self.comboBox_sightlines_observe_sightline_obstructions)
        form_layout_sightlines.addRow(qtw.QLabel("Examples: Building(s), Rail/Road Alignment, Commercial Signing, Unattended Railway Equipment, Topography, Traffic Control Devices, Utilities, Vegetation)"))
        form_layout_sightlines.addRow('Sightline Comments', self.textEdit_sightlines_comments)

        # layout container widgets - SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', self.label_signs_and_markings_advisory_speed_comments)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_advisory_speed_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_advisory_speed_s_or_w_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', self.label_signs_and_markings_comments)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_dividing_lines_present)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', self.label_signs_and_markings_emergency_notification_comments
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_condition)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_legible)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_orientation)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_condition)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_legible)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_orientation)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_present)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', self.label_signs_and_markings_number_of_tracks_comments)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_per_mutcd)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_posted_speed_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_posted_speed_s_or_w_approach_present)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', self.label_signs_and_markings_railway_crossing_ahead_comments)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_rail)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_road)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_height)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_rail)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_road)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_height)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', self.label_signs_and_markings_railway_crossing_comments)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_railway_crossing_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_railway_crossing_s_or_w_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_sidewalks_present)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', self.label_signs_and_markings_stop_comments)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_height)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_location_from_rail)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_location_from_road)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_stop_n_or_e_approach_per_fig_8_4)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_stop_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_stop_n_or_e_approach_same_post)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_height)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_location_from_rail)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_location_from_road)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_stop_s_or_w_approach_per_fig_8_4)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_stop_s_or_w_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_stop_s_or_w_approach_same_post)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', self.label_signs_and_markings_stop_sign_ahead_comments)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_height)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_rail)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_road)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_height)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_rail)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_road)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_present)

        # layout container widgets - GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
        form_layout_gcws_warrants.addRow(qtw.QLabel('Warrants for a Warning System Without Gates (Public Crossings)'))
        form_layout_gcws_warrants.addRow(qtw.QLabel('If any of A through D below are met, then a warning system without gates is required'))
        form_layout_gcws_warrants.addRow('A. Where the forecast cross-product is 2,000 or more:', self.label_gcws_warrant_public_9_1_a)
        form_layout_gcws_warrants.addRow('B. Where there is no sidewalk, path or trail and the railway design speed is more than 129 km/hr (80 mph);', self.label_gcws_warrant_public_9_1_b)
        form_layout_gcws_warrants.addRow('C. Where there is a sidewalk, path or trail and the railway design speed is more than 81 km/hr (50 mph);', self.label_gcws_warrant_public_9_1_c)
        form_layout_gcws_warrants.addRow(qtw.QLabel('D. Where the railway design speed is more than 25 km/hr (15 mph) but less than the railway design speed referred to in (b) or (c), and'))
        form_layout_gcws_warrants.addRow('D1. Where there are two or more lines of railway where railway equipment may pass each other;', self.label_gcws_warrant_public_9_1_d_i)
        form_layout_gcws_warrants.addRow('D2. The distance as shown in Figure 9-1(a) between a Stop sign at an intersection and the nearest rail in the crossing surface is less than 30m;', self.label_gcws_warrant_public_9_1_d_ii)
        form_layout_gcws_warrants.addRow('D3. In the case of an intersection with a traffic signal, the distance between the stop line of the intersection and the nearest rail in the crossing surface, as shown in Figure 9-1(b), is less than 60m, or where there is no stop line, the distance between the travelled way and the nearest rail in the crossing surface is less than 60m.', self.label_gcws_warrant_public_9_1_d_iii)
        form_layout_gcws_warrants.addRow(qtw.QLabel('Warrants for a Warning System Without Gates (Private Crossings)'))
        form_layout_gcws_warrants.addRow(qtw.QLabel('If any of A through B below are met, then a warning system without gates is required'))
        form_layout_gcws_warrants.addRow('A. Where the forecast cross-product is 2,000 or more;', self.label_gcws_warrant_private_9_3_1)
        form_layout_gcws_warrants.addRow(qtw.QLabel('B. Where the railway design speed is more than 25 km/hr (15mph), and;'))
        form_layout_gcws_warrants.addRow('B1. The forecast cross-product is 100 or more and there are two or more lines of railway where railway equipment may pass each other;', self.label_gcws_warrant_private_9_3_2_a)
        form_layout_gcws_warrants.addRow('B2. The forecast cross-product is 100 or more and grade crossing does not include a sidewalk, path or trail and the railway design speed is more than 129 km/hr (80mph);', self.label_gcws_warrant_private_9_3_2_b)
        form_layout_gcws_warrants.addRow('B3. The grade crossing does includes a sidewalk, path or trail and the railway design speed is more than 81 km/hr (50mph);', self.label_gcws_warrant_private_9_3_2_c)
        form_layout_gcws_warrants.addRow(qtw.QLabel('Warrants for a Warning System Without Gates (Grade Crossings for a Sidewalk, Path, or Trail)'))
        form_layout_gcws_warrants.addRow(qtw.QLabel('If A below is met, then a warning system without gates is required'))
        form_layout_gcws_warrants.addRow('A. The sidewalk, path or trail is outside the island circuit of an adjacent warning system and the railway design speed is more than 81 km/hr (50mph)', self.label_gcws_warrant_sidewalk_9_5)
        form_layout_gcws_warrants.addRow(qtw.QLabel('Warrants for a Warning System With Gates (Public Crossings)'))
        form_layout_gcws_warrants.addRow(qtw.QLabel('If a warning system is warranted, and any of A through F are met, then gates are also required'))
        form_layout_gcws_warrants.addRow('A. A warning system is required under 9.1, and;', self.label_gcws_warrant_public_9_1)
        form_layout_gcws_warrants.addRow('B. The forecast cross-product is 50,000 or more;', self.label_gates_gcws_warrant_public_9_2_1_a)
        form_layout_gcws_warrants.addRow('C. There are two or more lines of railway where railway equipment may pass each other;', self.label_gates_gcws_warrant_public_9_2_1_b)
        form_layout_gcws_warrants.addRow('D. The railway design speed is more than 81 km/hr (50mph);', self.label_gates_gcws_warrant_public_9_2_1_c)
        form_layout_gcws_warrants.addRow('E. The distance as shown in Figure 9-1(a) between a Stop sign at an intersection and the nearest rail in the crossing surface is less than 30m;', self.label_gates_gcws_warrant_public_9_2_1_d)
        form_layout_gcws_warrants.addRow('F. In the case of an intersection with a traffic signal, the distance between the stop line of the intersection and the nearest rail in the crossing surface, as shown in Figure 9-1(b), is less than 60m, or where there is no stop line, the distance between the travelled way and the nearest rail in the crossing surface is less than 60m.', self.label_gates_gcws_warrant_public_9_2_1_e)
        form_layout_gcws_warrants.addRow(qtw.QLabel('Warrants for a Warning System With Gates (Private Crossings)'))
        form_layout_gcws_warrants.addRow(qtw.QLabel('If a warning system is warranted, and any of A through D are met, then gates are also required'))
        form_layout_gcws_warrants.addRow('A. A warning system is required under 9.1, and;', self.label_gcws_warrant_private_9_3)
        form_layout_gcws_warrants.addRow('B. The forecast cross-product is 50,000 or more;', self.label_gates_gcws_warrant_private_9_4_1_a)
        form_layout_gcws_warrants.addRow('C. There are two or more lines of railway where railway equipment may pass each other;', self.label_gates_gcws_warrant_private_9_4_1_b)
        form_layout_gcws_warrants.addRow('D. The railway design speed is more than 81 km/hr (50mph);', self.label_gates_gcws_warrant_private_9_4_1_c)
        form_layout_gcws_warrants.addRow(qtw.QLabel('Warrants for a Warning System With Gates (Grade Crossings for a Sidewalk, Path, or Trail)'))
        form_layout_gcws_warrants.addRow('', self.label_gates_gcws_warrant_sidewalk_9_6)
        form_layout_gcws_warrants.addRow('GCWS Warrants Comments', self.textEdit_gcws_warrants_comments)

        # layout container widgets - GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
        form_layout_gcws.addRow('Design Approach Warning Time:', self.label_gcws_rail_design_approach_warning_time)
        form_layout_gcws.addRow(qtw.QLabel('Should be greatest of:'))
        form_layout_gcws.addRow('a. 20 s, unless the grade crossing clearance distance (Fig 10-1) is more than 11 m (35 ft), in which case, the 20 s must be increased by one second for each additional 3 m (10 ft), or fraction thereof;', self.label_gcws_rail_design_warning_time_clearance_distance)
        form_layout_gcws.addRow("b. The Departure Time for the grade crossing 'design vehicle' (Article 10.3.2);", self.label_gcws_rail_design_warning_time_departure_time_vehicle)
        form_layout_gcws.addRow('c. The Departure Time for pedestrians, cyclists, and persons using assistive devices (Article 10.3.3);', self.label_gcws_rail_design_warning_time_departure_time_pedestrian)
        form_layout_gcws.addRow('d. The gate arm clearance time, plus the time to complete the gate arm descent, plus 5 seconds;', self.label_gcws_rail_design_warning_time_gate_arm_clearance)
        form_layout_gcws.addRow('e. The minimum warning time required for traffic signal pre-emption;', self.spinBox_gcws_rail_design_warning_time_preemption)
        form_layout_gcws.addRow('f. The time for the design vehicle travelling at the design speed to travel from the stopping sight distance, as specified in article 1.2.5.2 of the Geometric Design Guide and pass completely through the clearance distance;', self.label_gcws_rail_design_warning_time_ssd)
        form_layout_gcws.addRow('g. Adjacent Track Interconnected Highway-Rail Grade Crossing. (add to (a), - (e))', self.label_gcws_rail_design_warning_time_adjacent_crossing)
        form_layout_gcws.addRow('Actual Approach Warning Time:', self.doubleSpinBox_gcws_rail_crossing_warning_time_actual)
        form_layout_gcws.addRow(qtw.QLabel('Warning Systems Clearance Distance from Railway (Min. 3.66 m (12 ft) for signal mast or 3.05 m (10 ft) for end of gate arm; from centreline of track) (m):'))
        form_layout_gcws.addRow('N or E Road Approach:', self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_from_rail)
        form_layout_gcws.addRow('S or W Road Approach:', self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_from_rail)
        form_layout_gcws.addRow(qtw.QLabel('Warning System Clearance Distance from Roadway (Min. 625 mm from curb; or 1.875 m from travelled way and 625 mm from shoulder) (m)'))
        form_layout_gcws.addRow('N or E Road Approach:', self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_from_road)
        form_layout_gcws.addRow('S or W Road Approach:', self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_from_road)
        form_layout_gcws.addRow(qtw.QLabel('Distance between top of foundation and surrounding ground level (max. 100 mm (4 in))'))
        form_layout_gcws.addRow('N or E Road Approach:', self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_top_of_foundation)
        form_layout_gcws.addRow('S or W Road Approach:', self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_top_of_foundation)
        form_layout_gcws.addRow(qtw.QLabel('Is the slope of surrounding ground from foundation towards the travelled way less than 25% (4:1)?'))
        form_layout_gcws.addRow('N or E Road Approach:', self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_slope_from_foundation)
        form_layout_gcws.addRow('S or W Road Approach:', self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_slope_from_foundation)
        form_layout_gcws.addRow(qtw.QLabel('Light units:'))
        form_layout_gcws.addRow('N or E Road Approach:', self.comboBox_gcws_observe_light_units_n_or_e_approach)
        form_layout_gcws.addRow('S or W Road Approach:', self.comboBox_gcws_observe_light_units_s_or_w_approach)
        form_layout_gcws.addRow('Condition:', self.comboBox_gcws_observe_light_units_condition)
        form_layout_gcws.addRow(qtw.QLabel('Cantilever Lights:'))
        form_layout_gcws.addRow('N or E Road Approach:', self.comboBox_gcws_observe_cantilever_lights_n_or_e_approach)
        form_layout_gcws.addRow('S or W Road Approach:', self.comboBox_gcws_observe_cantilever_lights_s_or_w_approach)
        form_layout_gcws.addRow('Condition:', self.comboBox_gcws_observe_cantilever_lights_condition)
        form_layout_gcws.addRow('If there is only one sidewalk, is a bell located on the adjacent assembly?', self.comboBox_gcws_observe_bell_if_sidewalk)
        form_layout_gcws.addRow(qtw.QLabel('Bells:'))
        form_layout_gcws.addRow('N or E Road Approach:', self.comboBox_gcws_observe_bells_n_or_e_approach)
        form_layout_gcws.addRow('S or W Road Approach:', self.comboBox_gcws_observe_bells_s_or_w_approach)
        form_layout_gcws.addRow('Condition:', self.comboBox_gcws_observe_bells_condition)
        form_layout_gcws.addRow(qtw.QLabel('Gates:'))
        form_layout_gcws.addRow('N or E Road Approach:', self.comboBox_gcws_observe_gates_n_or_e_approach)
        form_layout_gcws.addRow('S or W Road Approach:', self.comboBox_gcws_observe_gates_s_or_w_approach)
        form_layout_gcws.addRow('Condition:', self.comboBox_gcws_observe_gates_condition)
        form_layout_gcws.addRow('Is crossing warning system equipped with monitoring devices that gather and retain the data and time of information (per 12.2) for a min. of 30 days?', self.comboBox_gcws_rail_self_diagnostic)
        form_layout_gcws.addRow('Does crossing warning system provide consitent warning times for railway equipment regularly operating over the grade crossing?', self.comboBox_gcws_observe_warning_time_consistency)
        form_layout_gcws.addRow('Where Railway Design Speed has been reduced, other than TSO, does actual Crossing Warning Time exceed 13s compared with design?', self.comboBox_gcws_observe_warning_time_consistency_reduced_speed)
        form_layout_gcws.addRow('Where railway eqipment regularly stops, left standing or turnout present within limits of warning systems, are Cut-Out Circuits in place?', self.comboBox_gcws_rail_cut_out_circuit_requirements)
        form_layout_gcws.addRow('If Directional Stick Circuits present, are requirments of GCS 16.4 met?', self.comboBox_gcws_rail_directional_stick_circuit_requirements)
        form_layout_gcws.addRow('Limited Use Warning System without Walk Light Assembly (Y/N)? (For Private Crossing with fewer than 3 residential dwellings only)', self.comboBox_gcws_observe_gcws_limited_use_without_walk_light_assembly)
        form_layout_gcws.addRow('Limited Use Warning System with Walk Light Assembly (Y/N)? (For Private Crossing and restricted access only)', self.comboBox_gcws_observe_gcws_limited_use_with_walk_light_assembly)
        form_layout_gcws.addRow('GCWS Comments', self.textEdit_gcws_comments)
        
        # layout container widgets - FLASHING LIGHT UNITS (GCS SECTION 13 & 14)
        form_layout_gcws_lights.addRow('Are signal assemblies as shown in Figure 12-1?', self.comboBox_light_units_observe_per_fig_12_1)
        form_layout_gcws_lights.addRow(qtw.QLabel('Alignment Height (m)'))
        form_layout_gcws_lights.addRow('N or E Road Approach:', self.doubleSpinBox_light_units_measure_n_or_e_approach_height)
        form_layout_gcws_lights.addRow('S or W Road Approach:', self.doubleSpinBox_light_units_measure_s_or_w_approach_height)
        form_layout_gcws_lights.addRow(qtw.QLabel('Are primary light units visible for at least the minimum SSD?'))
        form_layout_gcws_lights.addRow('N or E Road Approach:', self.comboBox_light_units_observe_visibility_front_lights_n_or_e_approach)
        form_layout_gcws_lights.addRow('S or W Road Approach:', self.comboBox_light_units_observe_visibility_front_lights_s_or_w_approach)
        form_layout_gcws_lights.addRow(qtw.QLabel('Are additional light units required to cover intermediate areas of the road approaches?'))
        form_layout_gcws_lights.addRow('N or E Road Approach:', self.comboBox_light_units_observe_supplemental_lights_n_or_e_approach)
        form_layout_gcws_lights.addRow('S or W Road Approach:', self.comboBox_light_units_observe_supplemental_lights_s_or_w_approach)
        form_layout_gcws_lights.addRow(qtw.QLabel('Are back light units visible by stopped vehicles at least 15 m?'))
        form_layout_gcws_lights.addRow('N or E Road Approach:', self.comboBox_light_units_observe_visibility_back_lights_n_or_e_approach)
        form_layout_gcws_lights.addRow('S or W Road Approach:', self.comboBox_light_units_observe_visibility_back_lights_s_or_w_approach)
        form_layout_gcws_lights.addRow(qtw.QLabel('Are lights installed exclusively for sidewalks, paths or trails visible for at least 30 m?'))
        form_layout_gcws_lights.addRow('N or E Rail Approach:', self.comboBox_light_units_observe_sidewalks_n_or_e_approach)
        form_layout_gcws_lights.addRow('S or W Rail Approach:', self.comboBox_light_units_observe_sidewalks_s_or_w_approach)
        form_layout_gcws_lights.addRow('Are cantilevers as shown in Figure 12-3?', self.comboBox_light_units_observe_cantilevers_per_fig_12_3)
        form_layout_gcws_lights.addRow(qtw.QLabel('Distance from nearest rail (m)'))
        form_layout_gcws_lights.addRow('N or E Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_distance_from_rail)
        form_layout_gcws_lights.addRow('S or W Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_distance_from_rail)
        form_layout_gcws_lights.addRow(qtw.QLabel('Distance from travelled way (m)'))
        form_layout_gcws_lights.addRow('N or E Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_distance_from_road)
        form_layout_gcws_lights.addRow('S or W Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_distance_from_road)
        form_layout_gcws_lights.addRow(qtw.QLabel('Height (m)'))
        form_layout_gcws_lights.addRow('N or E Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_height)
        form_layout_gcws_lights.addRow('S or W Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_height)
        form_layout_gcws_lights.addRow(qtw.QLabel('DR (m)'))
        form_layout_gcws_lights.addRow('N or E Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_dr)
        form_layout_gcws_lights.addRow('S or W Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_dr)
        form_layout_gcws_lights.addRow(qtw.QLabel('DL (m)'))
        form_layout_gcws_lights.addRow('N or E Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_dl)
        form_layout_gcws_lights.addRow('S or W Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_dl)
        form_layout_gcws_lights.addRow('Light Unit Comments:', self.textEdit_light_units_comments)

        # layout container widgets - GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
        form_layout_gcws_gates.addRow('Gate Arm Delay Time (from Plans) (s):', self.doubleSpinBox_gates_gcws_rail_gate_arm_delay_time_design)
        form_layout_gcws_gates.addRow('Gate Arm Descent Time (from Plans) (s):', self.doubleSpinBox_gates_gcws_rail_gate_arm_descent_time_design)
        form_layout_gcws_gates.addRow('Inner Gate Arm Delay Time for Adjacent Track Interconnected Highway-Rail Grade Crossing (Recommended) (s):', self.label_gates_gcws_calculate_inner_gate_arm_delay_time_recommended)
        form_layout_gcws_gates.addRow('Inner Gate Arm Delay Time for Adjacent Track Interconnected Highway-Rail Grade Crossing (from Plans) (s):', self.doubleSpinBox_gates_gcws_rail_inner_gate_arm_delay_time_design)
        form_layout_gcws_gates.addRow('Measure Gate Ascent Time (Actual) (s):', self.doubleSpinBox_gates_gcws_measure_gate_ascent_time)
        form_layout_gcws_gates.addRow('Measure Gate Descent Time (Actual) (s):', self.doubleSpinBox_gates_gcws_measure_gate_descent_time)
        form_layout_gcws_gates.addRow('Check Gate Ascent Time (6 to 12 sec):', self.comboBox_gates_gcws_observe_gate_ascent_time)
        form_layout_gcws_gates.addRow('Check Gate Descent Time (10 to 15 sec):', self.comboBox_gates_gcws_observe_gate_descent_time)
        form_layout_gcws_gates.addRow('Does gate arm come to rest in the horizontal position not less than 5s before the arrival at the crossing of railway equipment?:', self.comboBox_gates_gcws_observe_gate_arm_rest)
        form_layout_gcws_gates.addRow('Are gates as shown in Figure 12-2?', self.comboBox_gates_gcws_observe_per_fig_12_2)
        form_layout_gcws_gates.addRow(qtw.QLabel('Are strips on the gate arm 406 mm (16 in.) wide and aligned vertically?'))
        form_layout_gcws_gates.addRow('N or E Road Approach:', self.comboBox_gates_gcws_observe_gate_strips_n_or_e_approach)
        form_layout_gcws_gates.addRow('S or W Road Approach:', self.comboBox_gates_gcws_observe_gate_strips_s_or_w_approach)
        form_layout_gcws_gates.addRow(qtw.QLabel('Distance between the end of the gate arm and the longitudinal axis of the road approach (m)?'))
        form_layout_gcws_gates.addRow('N or E Road Approach:', self.doubleSpinBox_gates_gcws_measure_distance_between_gate_end_and_road_cl_n_or_e_approach)
        form_layout_gcws_gates.addRow('S or W Road Approach:', self.doubleSpinBox_gates_gcws_measure_distance_between_gate_end_and_road_cl_s_or_w_approach)
        form_layout_gcws_gates.addRow('Gates for GCWS Comments', self.textEdit_gates_gcws_comments)

        # layout container widgets - PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
        form_layout_aaws.addRow(qtw.QLabel('Are Prepare to Stop at Railway Crossing Sign present?'))
        form_layout_aaws.addRow('N or E Road Approach:', self.comboBox_aawd_observe_present_n_or_e_approach)
        form_layout_aaws.addRow('S or W Road Approach:', self.comboBox_aawd_observe_present_s_or_w_approach)
        form_layout_aaws.addRow(qtw.QLabel('Warrants for a Prepare to Stop at Railway Crossing Sign Per GCR'))
        form_layout_aaws.addRow('A. Is the roadway classified as an expressway?', self.label_aawd_warrant_gcr_lookup_road_classification)
        form_layout_aaws.addRow('B. Is at least one set of front lights on the warning system not clearly visible within the stopping sight distance of at least one of the lanes of the road approach?', self.comboBox_aawd_warrant_gcr_observe_sightline_obstruction)
        form_layout_aaws.addRow('C. Do weather conditions at the grade crossing repeatedly obscure the visibility of the warning system?', self.comboBox_aawd_warrant_gcr_observe_environmental_condition)
        form_layout_aaws.addRow(qtw.QLabel('Warrants for a Prepare to Stop at Railway Crossing Sign Per MUTCD'))
        form_layout_aaws.addRow('D. Is the speed limit of the travelled way greater than 90 km/h?', self.label_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr)
        form_layout_aaws.addRow('E. Is the crossing at the bottom of a hill or downgrade of considerable length?', self.comboBox_aawd_warrant_mutcd_lookup_significant_road_downgrade)
        form_layout_aaws.addRow(qtw.QLabel('Design AAWD Advance Activation Time (s):'))
        form_layout_aaws.addRow('N or E Road Approach:', self.label_aawd_calculate_advance_activation_time_design_n_or_e_approach)
        form_layout_aaws.addRow('S or W Road Approach:', self.label_aawd_calculate_advance_activation_time_design_s_or_w_approach)
        form_layout_aaws.addRow(qtw.QLabel('Recommended minimum Advance Warning Flasher Distance from Railway'))
        form_layout_aaws.addRow('N or E Road Approach:', self.label_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended)
        form_layout_aaws.addRow('S or W Road Approach:', self.label_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended)
        form_layout_aaws.addRow(qtw.QLabel('Actual Advance Warning Flasher Distance from Railway'))
        form_layout_aaws.addRow('N or E Road Approach:', self.doubleSpinBox_aawd_measure_distance_sign_and_stop_n_or_e_approach_actual)
        form_layout_aaws.addRow('S or W Road Approach:', self.doubleSpinBox_aawd_measure_distance_sign_and_stop_s_or_w_approach_actual)
        form_layout_aaws.addRow(qtw.QLabel('Does the advance activation time provide sufficient time for a vehicle to:'))
        form_layout_aaws.addRow(qtw.QLabel('a) clear the grade crossing before the arrival of railway equipment at the crossing surface (FLB)'))
        form_layout_aaws.addRow(qtw.QLabel('b) clear the grade crossing before gate arms start to descend (FLBG)'))
        form_layout_aaws.addRow('N or E Road Approach:', self.comboBox_aawd_road_aawd_sufficient_activation_time_n_or_e_approach)
        form_layout_aaws.addRow('S or W Road Approach:', self.comboBox_aawd_road_aawd_sufficient_activation_time_s_or_w_approach)
        form_layout_aaws.addRow('Prepare to Stop at Railway Crossing Sign Comments', self.textEdit_aawd_comments)

        # layout container widgets - INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
        form_layout_interconnection_traffic_signals.addRow(qtw.QLabel('Warrants for an Interconnected Traffic Signal'))
        form_layout_interconnection_traffic_signals.addRow('Is there less than 30m between the nearest rail of a grade crossing and the travelled way of an intersection with traffic signals?', self.label_preemption_of_traffic_signals_lookup_proximity_condition)
        form_layout_interconnection_traffic_signals.addRow('Is an Interconnected Traffic Signal required?', self.label_preemption_of_traffic_signals_lookup_required)
        form_layout_interconnection_traffic_signals.addRow(qtw.QLabel('Other Queuing Condition(s)'))
        form_layout_interconnection_traffic_signals.addRow('Is "D" insufficient such that road vehicles might queue onto the rail tracks? (I.E. less than 60 m for traffic signals; 30 m or more for a Stop sign (or 60 m or more for traffic signals) with queued traffic encroaching within 2.4 m of the nearest rail; a situation causing vehicles to routinely queue closer than 2.4 m to the nearest rail in the crossing (Example(s): Yield sign, a roundabout, a pedestrian crossing, a bikeway, or a stopped vehicle waiting to make left turn))', self.comboBox_preemption_of_traffic_signals_observe_queuing_condition)
        form_layout_interconnection_traffic_signals.addRow('Are adjacent traffic signals interconnected with a grade crossing warning system?', self.comboBox_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type)
        form_layout_interconnection_traffic_signals.addRow('Design Preemption activation warning time required for traffic signal preemption (s):', self.spinBox_preemption_of_traffic_signals_road_preemption_warning_time_design)
        form_layout_interconnection_traffic_signals.addRow('Actual Preemption activation warning time required for traffic signal preemption (s):', self.spinBox_preemption_of_traffic_signals_road_preemption_warning_time_actual)
        form_layout_interconnection_traffic_signals.addRow(qtw.QLabel('Field checks:'))
        #form_layout_interconnection_traffic_signals.addRow('Date of last pre-emption check?', self.label_preemption_of_traffic_signals_road_date_Last_preemption_check)
        form_layout_interconnection_traffic_signals.addRow('Does interconnection provide adequate time to clear traffic from the grade crossing before the arrival of railway equipment?', self.comboBox_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate)
        form_layout_interconnection_traffic_signals.addRow('Does interconnection prohibit road traffic from moving from the street intersection towards the grade crossing?', self.comboBox_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals)
        form_layout_interconnection_traffic_signals.addRow('Are there known queuing issues at the tracks?', self.comboBox_preemption_of_traffic_signals_observe_known_queuing_issues)
        form_layout_interconnection_traffic_signals.addRow('Are pedestrians accommodated during the pre-emption?', self.comboBox_preemption_of_traffic_signals_observe_pedestrian_accommodation)
        form_layout_interconnection_traffic_signals.addRow('Have longer/slower vehicles been considered (compared to Design Vehicle)?', self.comboBox_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles)       
        form_layout_interconnection_traffic_signals.addRow('Are supplemental signs needed for motorists (no right turn on red light, etc)?', self.comboBox_preemption_of_traffic_signals_observe_supplemental_signage)
        form_layout_interconnection_traffic_signals.addRow('Preemption of Traffic Signals Comments', self.textEdit_preemption_of_traffic_signals_comments)

        # layout container widgets - WHISTLE CESSATION (GCS SECTION Appendix D)
        form_layout_whistle_cessation.addRow('Is train whistling prohibited at this crossing?', self.comboBox_areas_without_train_whistling_rail_anti_whistling_zone)
        form_layout_whistle_cessation.addRow('24 hours per day?', self.comboBox_areas_without_train_whistling_rail_anti_whistling_zone_24_hrs)
        form_layout_whistle_cessation.addRow(qtw.QLabel('Requirements'))
        form_layout_whistle_cessation.addRow('Is there evidence of routine unauthorized access (trespassing) on the rail line in the area of the crossing? Comment below.', self.comboBox_areas_without_train_whistling_observe_trespassing_area)
        form_layout_whistle_cessation.addRow('What is the required type of warning system as per Table D-1?', self.label_areas_without_train_whistling_requirements_lookup_table_d1_criteria)
        form_layout_whistle_cessation.addRow('Are the requirements of Table D-1 met?', self.label_areas_without_train_whistling_requirements_observe_table_D1)
        form_layout_whistle_cessation.addRow('Further to Column A of Table D-1, is a crossing warning system with gates installed per GCS 9.2?', self.label_areas_without_train_whistling_lookup_gcs_9_2)
        form_layout_whistle_cessation.addRow('Does crossing warning system meet requirements of GCS 12-16?', self.comboBox_areas_without_train_whistling_lookup_gcs_12_to_16)
        form_layout_whistle_cessation.addRow('If Stop and Proceed, is crossing equipped with FLB meeting GCS 12-16 or manually protected?', self.comboBox_areas_without_train_whistling_observe_for_stop_and_proceed)       
        form_layout_whistle_cessation.addRow('Whistle Cessation Comments', self.textEdit_areas_without_train_whistling_comments)


        '''
        #######################
        # Size Control Layout #
        #######################

        # use stretch factor

        stretch_layout = qtw.QHBoxLayout()
        main_layout.addLayout(stretch_layout)
        stretch_layout.addWidget(qtw.QLineEdit('Short'), 1)
        stretch_layout.addWidget(qtw.QLineEdit('Long'), 2)
        
        ######################
        # The central widget #
        ######################
        self.textedit = qtw.QTextEdit()
        self.setCentralWidget(self.textedit)

        #################
        # The Statusbar #
        #################

        # The long way 'round
        #status_bar = qtw.QStatusBar()
        #self.setStatusBar(status_bar)
        #status_bar.showMessage('Welcome to text_editor.py')

        # The short way 'round
        self.statusBar().showMessage('Welcome to text_editor.py')

        # add widgets to statusbar
        charcount_self.label = qtw.QLabel("chars: 0")
        self.textedit.textChanged.connect(
            lambda: charcount_self.label.setText(
                "chars: " +
                str(len(self.textedit.toPlainText()))
                )
            )
        self.statusBar().addPermanentWidget(charcount_self.label)

        ###############j
        # The menubar #
        ###############
        menubar = self.menuBar()

        # add submenus to a menu
        file_menu = menubar.addMenu('File')
        edit_menu = menubar.addMenu('Edit')
        help_menu = menubar.addMenu('Help')

        # add actions
        open_action = file_menu.addAction('Open')
        save_action = file_menu.addAction('Save')

        # add separator
        file_menu.addSeparator()

        # add an action with a callback
        # Errata:  The book contains this line:
        #quit_action = file_menu.addAction('Quit', self.destroy)
        # It should call self.close instead, like so:
        quit_action = file_menu.addAction('Quit', self.close)

        # connect to a Qt Slot
        edit_menu.addAction('Undo', self.textedit.undo)

        # create a QAction manually

        redo_action = qtw.QAction('Redo', self)
        redo_action.triggered.connect(self.textedit.redo)
        edit_menu.addAction(redo_action)

        ############################
        # The Toolbar and QActions #
        ############################

        toolbar = self.addToolBar('File')
        #toolbar.addAction(open_action)
        #toolbar.addAction("Save")

        toolbar.setMovable(False)
        toolbar.setFloatable(False)
        toolbar.setAllowedareas(
            qtc.Qt.topToolBararea |
            qtc.Qt.BottomToolBararea
        )

        # Add with icons
        open_icon = self.style().standardIcon(qtw.QStyle.SP_DirOpenIcon)
        save_icon = self.style().standardIcon(qtw.QStyle.SP_DriveHDIcon)

        open_action.setIcon(open_icon)
        toolbar.addAction(open_action)
        toolbar.addAction(
            save_icon,
            'Save',
            lambda: self.statusBar().showMessage('File Saved!')
        )

        # create a custom QAction

        help_action = qtw.QAction(
            self.style().standardIcon(qtw.QStyle.SP_DialogHelpButton),
            'Help',
            self,  # important to pass the parent!
            triggered=lambda: self.statusBar().showMessage(
                'Sorry, no help yet!'
            )
        )
        toolbar.addAction(help_action)

        # create a toolbar in another part of the screen:
        toolbar2 = qtw.QToolBar('Edit')
        self.addToolBar(qtc.Qt.RightToolBararea, toolbar2)
        toolbar2.addAction('Copy', self.textedit.copy)
        toolbar2.addAction('Cut', self.textedit.cut)
        toolbar2.addAction('Paste', self.textedit.paste)


        ################
        # Dock Widgets #
        ################

        dock = qtw.QDockWidget("Replace")
        self.addDockWidget(qtc.Qt.LeftDockWidgetarea, dock)

        # make it not closable
        dock.setFeatures(
            qtw.QDockWidget.DockWidgetMovable |
            qtw.QDockWidget.DockWidgetFloatable
        )

        replace_widget = qtw.QWidget()
        replace_widget.setLayout(qtw.QVBoxLayout())
        dock.setWidget(replace_widget)

        self.search_text_inp = qtw.QLineEdit(placeholderText='search')
        self.replace_text_inp = qtw.QLineEdit(placeholderText='replace')
        search_and_replace_btn = qtw.QPushButton(
            "Search and Replace",
            clicked=self.search_and_replace
            )
        replace_widget.layout().addRow(input_self.search_text_inp)
        replace_widget.layout().addRow(input_self.replace_text_inp)
        replace_widget.layout().addRow(input_search_and_replace_btn)
        replace_widget.layout().addStretch()

        ############################
        # Messageboxes and Dialogs #
        ############################

        # QMessageBox
        help_menu.addAction('About', self.showAboutDialog)

        if self.settings.value('show_warnings', False, type=bool):
            response = qtw.QMessageBox.question(
                self,
                'My Text Editor',
                'This is beta software, do you want to continue?',
                qtw.QMessageBox.Yes | qtw.QMessageBox.Abort
            )
            if response == qtw.QMessageBox.Abort:
                self.close()
                sys.exit()

            # custom message box

            splash_screen = qtw.QMessageBox()
            splash_screen.setWindowTitle('My Text Editor')
            splash_screen.setText('BETA SOFTWARE WARNING!')
            splash_screen.setInformativeText(
                'This is very, very beta, '
                'are you really sure you want to use it?'
            )
            splash_screen.setDetailedText(
                'This editor was written for pedagogical '
                'purposes, and probably is not fit for real work.'
            )
            splash_screen.setWindowModality(qtc.Qt.WindowModal)
            splash_screen.addButton(qtw.QMessageBox.Yes)
            splash_screen.addButton(qtw.QMessageBox.Abort)
            response = splash_screen.exec_()
            if response == qtw.QMessageBox.Abort:
                self.close()
                sys.exit()

        # QFileDialog
        open_action.triggered.connect(self.openFile)
        save_action.triggered.connect(self.saveFile)

        # QFontDialog

        edit_menu.addAction('Set Font…', self.set_font)

        # Custom dialog
        edit_menu.addAction('Settings…', self.show_settings)

        ###################
        # Saving Settings #
        ###################


        # end main UI code
        self.show()

    def search_and_replace(self):
        s_text = self.search_text_inp.text()
        r_text = self.replace_text_inp.text()

        if s_text:
            self.textedit.setText(
                self.textedit.toPlainText().replace(s_text, r_text)
                )

    def showAboutDialog(self):
        qtw.QMessageBox.about(
            self,
            "About text_editor.py",
            "This is a text editor written in PyQt5."
        )

    def openFile(self):
        filename, _ = qtw.QFileDialog.getOpenFileName(
            self,
            "Select a text file to open…",
            qtc.QDir.homePath(),
            'Text Files (*.txt) ;;Python Files (*.py) ;;All Files (*)',
            'Python Files (*.py)',
            qtw.QFileDialog.DontUseNativeDialog |
            qtw.QFileDialog.DontResolveSymlinks
        )
        if filename:
            try:
                with open(filename, 'r') as fh:
                    self.textedit.setText(fh.read())
            except Exception as e:
                # Errata:  Book contains the following line:
                #qtw.QMessageBox.critical(f"Could not load file: {e}")
                # It should read like this:
                qtw.QMessageBox.critical(self, f"Could not load file: {e}")

    def saveFile(self):
        filename, _ = qtw.QFileDialog.getSaveFileName(
            self,
            "Select the file to save to…",
            qtc.QDir.homePath(),
            'Text Files (*.txt) ;;Python Files (*.py) ;;All Files (*)'
        )
        if filename:
            try:
                with open(filename, 'w') as fh:
                    fh.write(self.textedit.toPlainText())
            except Exception as e:
                # Errata:  Book contains this line:
                #qtw.QMessageBox.critical(f"Could not save file: {e}")
                # It should read like this:
                qtw.QMessageBox.critical(self, f"Could not load file: {e}")

    def set_font(self):
        current = self.textedit.currentFont()
        font, accepted = qtw.QFontDialog.getFont(
            current,
            self,
            options=(
                qtw.QFontDialog.DontUseNativeDialog |
                qtw.QFontDialog.MonospacedFonts
            )
        )
        if accepted:
            self.textedit.setCurrentFont(font)

    def show_settings(self):

        settings_dialog = SettingsDialog(self.settings, self)
        settings_dialog.exec()
        '''
    