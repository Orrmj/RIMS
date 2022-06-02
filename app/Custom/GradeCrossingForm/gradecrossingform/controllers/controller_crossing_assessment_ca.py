import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtSql as qts

from gradecrossingform.models.model_crossing_assessment_ca import ModelCrossingAssessmentCA
from gradecrossingform.views.view_crossing_assessment_ca import ViewCrossingAssessmentCA
from GradeCrossingForm.db.db_crossing_assessment_ca import DBCrossingAssessmentCA

class controllerCrossingassessmentCA(qtw.QWidget):
    def __init__(self):
        super().__init__() # create default constructor for QWidget
        self.db = DBCrossingAssessmentCA()
        self.view = ViewCrossingAssessmentCA()
        self.model = ModelCrossingAssessmentCA(self.view)

        self.connect_and_emit_trigger()
        self.map_fields_to_sql()

    def connect_and_emit_trigger(self):
        #connecting a signal to python callables
        # collISION histoRY (5 year periOD)
        #connect signals and slots - collision_history_total_5_year_period
        '''
        Connect input variable signals to collision_history_total_5_year_period method slot.
        required input variables: 
            spinBox_collision_history_fatal_injury, spinBox_collision_history_personal_injury, spinBox_collision_history_property_damage
        Related methods:
            none
        '''
        self.view.spinBox_collision_history_fatal_injury.valueChanged.connect(self.model.collision_history_total_5_year_period)
        self.view.spinBox_collision_history_personal_injury.valueChanged.connect(self.model.collision_history_total_5_year_period)
        self.view.spinBox_collision_history_property_damage.valueChanged.connect(self.model.collision_history_total_5_year_period)
        
        #connect signals and slots - collision_history_risk_index_initial
        '''
        Connect input variable signals to collision_history_risk_index_initial method slot.
        required input variables: 
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
            general_info_rail_railway_design_speed
            general_info_rail_no_tracks_total
            general_info_rail_no_trains_per_day_total
            general_info_road_no_traffic_lanes_total
        '''
        self.view.spinBox_general_info_road_aadt_current.valueChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.spinBox_general_info_road_no_traffic_lanes_bidirectional.valueChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.spinBox_general_info_road_no_traffic_lanes_northbound_or_easttbound.valueChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound.valueChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.comboBox_inspection_details_gcws_type.currentTextChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.comboBox_general_info_road_classification.currentTextChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.comboBox_grade_crossing_surface_observe_road_approach_surface_type.currentTextChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.comboBox_gcws_observe_gates_n_or_e_approach.currentTextChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.comboBox_gcws_observe_gates_s_or_w_approach.currentTextChanged.connect(self.model.collision_history_risk_index_initial)
        
        #connect signals and slots - collision_history_risk_index_final
        '''
        Connect input variable signals to collision_history_risk_index_final method slot.
        required input variables: 
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
            general_info_rail_railway_design_speed
            general_info_rail_no_tracks_total
            general_info_rail_no_trains_per_day_total
            general_info_road_no_traffic_lanes_total
            collision_history_total_5_year_period
        '''

        self.view.spinBox_general_info_road_aadt_current.valueChanged.connect(self.model.collision_history_risk_index_final)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.collision_history_risk_index_final)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.collision_history_risk_index_final)
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.collision_history_risk_index_final)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.collision_history_risk_index_final)
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.collision_history_risk_index_final)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.collision_history_risk_index_final)
        self.view.spinBox_general_info_road_no_traffic_lanes_bidirectional.valueChanged.connect(self.model.collision_history_risk_index_final)
        self.view.spinBox_general_info_road_no_traffic_lanes_northbound_or_easttbound.valueChanged.connect(self.model.collision_history_risk_index_final)
        self.view.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound.valueChanged.connect(self.model.collision_history_risk_index_final)
        self.view.comboBox_inspection_details_gcws_type.currentTextChanged.connect(self.model.collision_history_risk_index_final)
        self.view.comboBox_general_info_road_classification.currentTextChanged.connect(self.model.collision_history_risk_index_final)
        self.view.comboBox_grade_crossing_surface_observe_road_approach_surface_type.currentTextChanged.connect(self.model.collision_history_risk_index_final)
        self.view.comboBox_gcws_observe_gates_n_or_e_approach.currentTextChanged.connect(self.model.collision_history_risk_index_final)
        self.view.comboBox_gcws_observe_gates_s_or_w_approach.currentTextChanged.connect(self.model.collision_history_risk_index_final)
        self.view.spinBox_collision_history_fatal_injury.valueChanged.connect(self.model.collision_history_risk_index_final)
        self.view.spinBox_collision_history_personal_injury.valueChanged.connect(self.model.collision_history_risk_index_final)
        self.view.spinBox_collision_history_property_damage.valueChanged.connect(self.model.collision_history_risk_index_final)

        # GEneRAL INforMATION
        #connect signals and slots - general_info_rail_no_tracks_total
        '''
        Connect input variable signals to general_info_rail_no_tracks_total method slot.
        required input variables: 
            spinBox_general_info_rail_no_tracks_main, spinBox_general_info_rail_no_tracks_other
        Related methods:
            none
        '''
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.general_info_rail_no_tracks_total)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.general_info_rail_no_tracks_total)
        
        #connect signals and slots - general_info_rail_no_trains_per_day_total
        '''
        Connect input variable signals to general_info_rail_no_trains_per_day_total method slot.
        required input variables: 
            spinBox_general_info_rail_no_trains_per_day_freight, spinBox_general_info_rail_no_trains_per_day_passengers
        Related methods:
            none
        '''
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.general_info_rail_no_trains_per_day_total)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.general_info_rail_no_trains_per_day_total)
        
        #connect signals and slots - general_info_road_no_traffic_lanes_total
        '''
        Connect input variable signals to general_info_road_no_traffic_lanes_total method slot.
        required input variables: 
            spinBox_general_info_road_no_traffic_lanes_bidirectional, spinBox_general_info_road_no_traffic_lanes_northbound_or_easttbound, spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound
        Related methods:
            none
        '''
        self.view.spinBox_general_info_road_no_traffic_lanes_bidirectional.valueChanged.connect(self.model.general_info_road_no_traffic_lanes_total)
        self.view.spinBox_general_info_road_no_traffic_lanes_northbound_or_easttbound.valueChanged.connect(self.model.general_info_road_no_traffic_lanes_total)
        self.view.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound.valueChanged.connect(self.model.general_info_road_no_traffic_lanes_total)
        
        #connect signals and slots - general_info_rail_railway_design_speed
        '''
        Connect input variable signals to general_info_rail_railway_design_speed method slot.
        required input variables: 
            spinBox_general_info_rail_max_railway_operating_speed_freight, spinBox_general_info_rail_max_railway_operating_speed_passenger
        Related methods:
            none
        '''
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.general_info_rail_railway_design_speed)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.general_info_rail_railway_design_speed)        
        
        # design consideRATIONS (GCS seCTION 10)
        #connect signals and slots - design_calculate_adjacent_track_clearance_time
        '''
        Connect input variable signals to design_calculate_adjacent_track_clearance_time method slot.
        required input variables: 
            doubleSpinBox_design_measture_adjacent_track_separation_distance, doubleSpinBox_design_measture_adjacent_track_clearance_distance
        Related methods:
            none
        '''
        self.view.doubleSpinBox_design_measture_adjacent_track_separation_distance.valueChanged.connect(self.model.design_calculate_adjacent_track_clearance_time)
        self.view.doubleSpinBox_design_measture_adjacent_track_clearance_distance.valueChanged.connect(self.model.design_calculate_adjacent_track_clearance_time)

        #connect signals and slots - design_calculate_clearance_time_crossing_pedestrian_design_check
        '''
        Connect input variable signals to design_calculate_clearance_time_crossing_pedestrian_design_check method slot.
        required input variables: 
            doubleSpinBox_design_measture_clearance_distance_pedestrian
        Related methods:
            none
        '''
        self.view.doubleSpinBox_design_measture_clearance_distance_pedestrian.valueChanged.connect(self.model.design_calculate_clearance_time_pedestrian_design_check)

        #connect signals and slots - design_calculate_clearance_time_vehicle_design_check
        '''
        Connect input variable signals to design_calculate_clearance_time_vehicle_design_check method slot.
        required input variables: 
            doubleSpinBox_design_measture_clearance_distance_pedestrian
            doubleSpinBox_design_measture_clearance_distance_vehicle
            doubleSpinBox_design_road_max_approach_grade_within_s
            combo_Box_design_road_design_vehicle_type        
        Related methods:
            design_input_reaction_time
            design_calculate_vehicle_departure_time_grade_adjusted
            design_calculate_vehicle_departure_time
            design_calculate_vehicle_travel_distance
            design_lookup_design_vehicle_length
            design_lookup_design_vehicle_class
            design_lookup_grade_adjustment_factor
        '''
        self.view.doubleSpinBox_design_measture_clearance_distance_pedestrian.valueChanged.connect(self.model.design_calculate_clearance_time_vehicle_design_check)
        self.view.doubleSpinBox_design_measture_clearance_distance_vehicle.valueChanged.connect(self.model.design_calculate_clearance_time_vehicle_design_check)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.design_calculate_clearance_time_vehicle_design_check)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_calculate_clearance_time_vehicle_design_check)                                                                     

        #TODO 
        #self.label_design_measture_clearance_distance_gate_arm_ssd = qtw.QLabel('no Value')

        #connect signals and slots - design_calculate_gate_arm_clearance_time_vehicle_ssd
        '''
        Connect input variable signals to design_calculate_gate_arm_clearance_time_vehicle_ssd method slot.
        required input variables: 
            spinBox_general_info_road_speed_design
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            comboBox_design_road_design_vehicle_type     
        Related methods:
            design_lookup_design_vehicle_length
            sightlines_lookup_ssd_minimum_n_or_e_approach
            sightlines_lookup_ssd_minimum_s_or_w_approach
        '''
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_ssd)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_ssd)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_ssd)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_ssd)

        #connect signals and slots - design_calculate_gate_arm_clearance_time_vehicle_stop
        '''
        Connect input variable signals to design_calculate_gate_arm_clearance_time_vehicle_stop method slot.
        required input variables:
            doubleSpinBox_design_measture_clearance_distance_pedestrian 
            doubleSpinBox_design_road_max_approach_grade_within_s
            comboBox_design_road_design_vehicle_type
        Related methods:
            label_design_input_reaction_time
            design_calculate_vehicle_departure_time_gate_arm_clearance
            design_lookup_grade_adjustment_factor
            design_lookup_design_vehicle_class
            design_lookup_design_vehicle_length
        '''
        self.view.doubleSpinBox_design_measture_clearance_distance_pedestrian.valueChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_stop)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_stop)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_stop)

        #connect signals and slots - design_calculate_gate_arm_clearance_time_vehicle_recommended
        '''
        Connect input variable signals to design_calculate_gate_arm_clearance_time_vehicle_recommended method slot.
        required input variables: 
            spinBox_general_info_road_speed_design
            doubleSpinBox_design_measture_clearance_distance_pedestrian
            doubleSpinBox_design_road_max_approach_grade_within_s
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach
            comboBox_design_road_design_vehicle_type
        Related methods:
            label_design_input_reaction_time
            design_calculate_gate_arm_clearance_time_vehicle_ssd
            design_calculate_gate_arm_clearance_time_vehicle_stop
            design_calculate_vehicle_departure_time_gate_arm_clearance
            design_lookup_design_vehicle_class
            design_lookup_design_vehicle_length
            design_lookup_grade_adjustment_factor
            sightlines_lookup_ssd_minimum_n_or_e_approach
            sightlines_lookup_ssd_minimum_s_or_w_approach
        '''
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_recommended)
        self.view.doubleSpinBox_design_measture_clearance_distance_pedestrian.valueChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_recommended)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_recommended)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_recommended)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_recommended)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_recommended)

        #connect signals and slots - design_calculate_vehicle_travel_distance
        '''
        Connect input variable signals to design_calculate_vehicle_travel_distance method slot.
        required input variables:
            doubleSpinBox_design_measture_clearance_distance_vehicle
            comboBox_design_road_design_vehicle_type
        Related methods:
            design_lookup_design_vehicle_length 
        ''' 
        self.view.doubleSpinBox_design_measture_clearance_distance_vehicle.valueChanged.connect(self.model.design_calculate_vehicle_travel_distance)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_calculate_vehicle_travel_distance)
        
        #connect signals and slots - design_calculate_vehicle_departure_time
        '''
        Connect input variable signals to design_calculate_vehicle_departure_time method slot.
        required input variables:
            doubleSpinBox_design_measture_clearance_distance_pedestrian
            doubleSpinBox_design_measture_clearance_distance_vehicle
            comboBox_design_road_design_vehicle_type
        Related methods:
            design_calculate_vehicle_travel_distance
            design_lookup_design_vehicle_class
            design_lookup_design_vehicle_length
        ''' 
        self.view.doubleSpinBox_design_measture_clearance_distance_pedestrian.valueChanged.connect(self.model.design_calculate_vehicle_departure_time)
        self.view.doubleSpinBox_design_measture_clearance_distance_vehicle.valueChanged.connect(self.model.design_calculate_vehicle_departure_time)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_calculate_vehicle_departure_time)

        #connect signals and slots - design_calculate_vehicle_departure_time_grade_adjusted
        '''
        Connect input variable signals to design_calculate_vehicle_departure_time_grade_adjusted method slot.
        required input variables:
           doubleSpinBox_design_measture_clearance_distance_pedestrian
           doubleSpinBox_design_measture_clearance_distance_vehicle
           doubleSpinBox_design_road_max_approach_grade_within_s
           comboBox_design_road_design_vehicle_type
        Related methods:
            design_calculate_vehicle_departure_time
            design_calculate_vehicle_travel_distance
            design_lookup_design_vehicle_class
            design_lookup_design_vehicle_length
            design_lookup_grade_adjustment_factor
        '''
        self.view.doubleSpinBox_design_measture_clearance_distance_pedestrian.valueChanged.connect(self.model.design_calculate_vehicle_departure_time_grade_adjusted)
        self.view.doubleSpinBox_design_measture_clearance_distance_vehicle.valueChanged.connect(self.model.design_calculate_vehicle_departure_time_grade_adjusted)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(lambda val:self.model.design_calculate_vehicle_departure_time_grade_adjusted)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_calculate_vehicle_departure_time_grade_adjusted)

        #connect signals and slots - design_calculate_vehicle_departure_time_gate_arm_clearance
        '''
        Connect input variable signals to design_calculate_vehicle_departure_time_gate_arm_clearance method slot.
        required input variables:
            comboBox_design_road_design_vehicle_type
        Related methods:    
            design_lookup_design_vehicle_class
            design_lookup_design_vehicle_length
        '''
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_calculate_vehicle_departure_time_gate_arm_clearance)
        
        #TODO
        #connect signals and slots - design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted
        '''
        Connect input variable signals to design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted method slot.
        required input variables:
            doubleSpinBox_design_road_max_approach_grade_within_s
            comboBox_design_road_design_vehicle_type
        Related methods:    
            design_calculate_vehicle_departure_time_gate_arm_clearance
            design_lookup_design_vehicle_class
            design_lookup_design_vehicle_length
            design_lookup_grade_adjustment_factor
        ''' 
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted)

        #connect signals and slots - design_lookup_design_vehicle_class
        '''
        Connect input variable signals to design_lookup_design_vehicle_class method slot.
        required input variables: 
            comboBox_design_road_design_vehicle_type
        Related methods:
            none
        ''' 
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_lookup_design_vehicle_class)

        #connect signals and slots - design_lookup_design_vehicle_length
        '''
        Connect input variable signals to design_lookup_design_vehicle_length method slot.
        required input variables: 
            comboBox_design_road_design_vehicle_type
        Related methods:
            none
        ''' 
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_lookup_design_vehicle_length)
                
        #connect signals and slots - design_lookup_grade_adjustment_factor
        '''
        Connect input variable signals to design_lookup_grade_adjustment_factor method slot.
        required input variables:
            doubleSpinBox_design_road_max_approach_grade_within_s
            comboBox_design_road_design_vehicle_type
        Related methods:
            none
        ''' 
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.design_lookup_grade_adjustment_factor)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_lookup_grade_adjustment_factor)

        #TODO
        #connect signals and slots - design_measture_clearance_distance_gate_arm_stop

        # road geomETRY (GCS seCTION 6)
        #connect signals and slots - road_geometry_lookup_gradient_difference
        '''
        Connect input variable signals to road_geometry_lookup_gradient_difference method slot.
        required input variables:
            comboBox_general_info_road_classification
        Related methods:
            none
        ''' 
        self.view.comboBox_general_info_road_classification.currentTextChanged.connect(self.model.road_geometry_lookup_gradient_difference)
        
        # sightLIneS (GCS seCTION 7)
        #connect signals and slots - sightlines_lookup_existing_active_crossing
        '''
        Connect input variable signals to sightlines_lookup_existing_active_crossing method slot.
        required input variables:
            comboBox_inspection_details_gcws_type
        Related methods:
            none
        ''' 
        self.view.comboBox_inspection_details_gcws_type.currentTextChanged.connect(self.model.sightlines_lookup_existing_active_crossing)
        
        #connect signals and slots - sightlines_lookup_existing_active_crossing_with_gates
        '''
        Connect input variable signals to sightlines_lookup_existing_active_crossing_with_gates method slot.
        required input variables:
            comboBox_inspection_details_gcws_type
            comboBox_gcws_observe_gates_n_or_e_approach
            comboBox_gcws_observe_gates_s_or_w_approach
        Related methods:
            none
        '''
        self.view.comboBox_inspection_details_gcws_type.currentTextChanged.connect(self.model.sightlines_lookup_existing_active_crossing_with_gates)
        self.view.comboBox_gcws_observe_gates_n_or_e_approach.currentTextChanged.connect(self.model.sightlines_lookup_existing_active_crossing_with_gates)
        self.view.comboBox_gcws_observe_gates_s_or_w_approach.currentTextChanged.connect(self.model.sightlines_lookup_existing_active_crossing_with_gates)

        # connect signals and slots - sightlines_calculate_dstopped_pedestrian_min_ft
        '''
        Connect input variable signals to sightlines_calculate_dstopped_pedestrian_min_ft method slot.
        required input variables:
            doubleSpinBox_design_measture_clearance_distance_pedestrian
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
        Related methods: 
            design_calculate_clearance_time_pedestrian_design_check       
            general_info_rail_railway_design_speed
        '''
        self.view.doubleSpinBox_design_measture_clearance_distance_pedestrian.valueChanged.connect(self.model.sightlines_calculate_dstopped_pedestrian_min_ft)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.sightlines_calculate_dstopped_pedestrian_min_ft)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.sightlines_calculate_dstopped_pedestrian_min_ft)

        #connect signals and slots - sightlines_calculate_dstopped_pedestrian_min_m
        '''
        Connect input variable signals to sightlines_calculate_dstopped_pedestrian_min_m method slot.
        required input variables:
            doubleSpinBox_design_measture_clearance_distance_pedestrian
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
        Related methods: 
            self.model.design_calculate_clearance_time_pedestrian_design_check       
            general_info_rail_railway_design_speed
        '''
        self.view.doubleSpinBox_design_measture_clearance_distance_pedestrian.valueChanged.connect(self.model.sightlines_calculate_dstopped_pedestrian_min_m)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.sightlines_calculate_dstopped_pedestrian_min_m)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.sightlines_calculate_dstopped_pedestrian_min_m)

        #TODO contains pedestrian clearance distance
        #connect signals and slots - sightlines_calculate_dstopped_vehicle_min_ft
        '''
        Connect input variable signals to sightlines_calculate_dstopped_vehicle_min_ft method slot.
        required input variables:
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            doubleSpinBox_design_measture_clearance_distance_pedestrian
            doubleSpinBox_design_measture_clearance_distance_vehicle
            doubleSpinBox_design_road_max_approach_grade_within_s
            comboBox_design_road_design_vehicle_type
        Related methods: 
            label_design_input_reaction_time
            general_info_rail_railway_design_speed
            design_calculate_clearance_time_vehicle_design_check
            design_calculate_vehicle_departure_time_grade_adjusted
            design_calculate_vehicle_departure_time
            design_lookup_design_vehicle_class
            design_calculate_vehicle_travel_distance
            design_lookup_grade_adjustment_factor
        '''
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_ft)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_ft)
        self.view.doubleSpinBox_design_measture_clearance_distance_pedestrian.valueChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_ft)
        self.view.doubleSpinBox_design_measture_clearance_distance_vehicle.valueChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_ft)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_ft)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_ft)

        #connect signals and slots - sightlines_calculate_dstopped_vehicle_min_m
        '''
        Connect input variable signals to sightlines_calculate_dstopped_vehicle_min_m method slot.
        required input variables:
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            doubleSpinBox_design_measture_clearance_distance_pedestrian
            doubleSpinBox_design_measture_clearance_distance_vehicle
            doubleSpinBox_design_road_max_approach_grade_within_s
            comboBox_design_road_design_vehicle_type
        Related methods: 
            label_design_input_reaction_time
            general_info_rail_railway_design_speed
            design_calculate_clearance_time_vehicle_design_check
            design_calculate_vehicle_departure_time_grade_adjusted
            design_calculate_vehicle_departure_time
            design_lookup_design_vehicle_class
            design_calculate_vehicle_travel_distance
            design_lookup_grade_adjustment_factor
        '''
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_m)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_m)
        self.view.doubleSpinBox_design_measture_clearance_distance_pedestrian.valueChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_m)
        self.view.doubleSpinBox_design_measture_clearance_distance_vehicle.valueChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_m)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_m)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_m)

        #connect signals and slots - sightlines_lookup_ssd_minimum_n_or_e_approach
        '''
        Connect input variable signals to sightlines_lookup_ssd_minimum_n_or_e_approach method slot.
        required input variables:
            spinBox_general_info_road_speed_design
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            comboBox_design_road_design_vehicle_type
        Related methods: 
            design_lookup_design_vehicle_class
        '''
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.sightlines_lookup_ssd_minimum_n_or_e_approach)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.sightlines_lookup_ssd_minimum_n_or_e_approach)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.sightlines_lookup_ssd_minimum_n_or_e_approach)

        #connect signals and slots - sightlines_lookup_ssd_minimum_s_or_w_approach
        '''
        Connect input variable signals to sightlines_lookup_ssd_minimum_s_or_w_approach method slot.
        required input variables:
            spinBox_general_info_road_speed_design
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach
            comboBox_design_road_design_vehicle_type
        Related methods: 
            design_lookup_design_vehicle_class
        '''
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.sightlines_lookup_ssd_minimum_s_or_w_approach)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.sightlines_lookup_ssd_minimum_s_or_w_approach)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.sightlines_lookup_ssd_minimum_s_or_w_approach)

        #connect signals and slots - sightlines_calculate_dssd_vehicle_min_ft
        '''
        Connect input variable signals to sightlines_calculate_dssd_vehicle_min_ft method slot.
        required input variables:
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_road_speed_design
            doubleSpinBox_design_measture_clearance_distance_vehicle
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach
            comboBox_design_road_design_vehicle_type 
        Related methods: 
            design_lookup_design_vehicle_class
            design_lookup_design_vehicle_length
            general_info_rail_railway_design_speed
            sightlines_lookup_ssd_minimum_n_or_e_approach
            sightlines_lookup_ssd_minimum_s_or_w_approach
        '''
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_ft)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_ft)
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_ft)
        self.view.doubleSpinBox_design_measture_clearance_distance_vehicle.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_ft)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_ft)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_ft)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_ft)
        
        #connect signals and slots - sightlines_calculate_dssd_vehicle_min_m
        '''
        Connect input variable signals to sightlines_calculate_dssd_vehicle_min_m method slot.
        required input variables:
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_road_speed_design
            doubleSpinBox_design_measture_clearance_distance_vehicle
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach
            comboBox_design_road_design_vehicle_type 
        Related methods: 
            design_lookup_design_vehicle_class
            design_lookup_design_vehicle_length
            general_info_rail_railway_design_speed
            sightlines_lookup_ssd_minimum_n_or_e_approach
            sightlines_lookup_ssd_minimum_s_or_w_approach
        '''
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_m)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_m)
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_m)
        self.view.doubleSpinBox_design_measture_clearance_distance_vehicle.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_m)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_m)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_m)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_m)

        # grade CROSSING warnING systEM warrANTS (GCS seCTION 9)
        #TODO
        #connect signals and slots - gcws_warrant_private_9_3
        # .valueChanged.connect(self.gcws_warrant_private_9_3)

        #connect signals and slots - gcws_warrant_private_9_3_1
        '''
        Connect input variable signals to gcws_warrant_private_9_3_1 method slot.
        required input variables:
            spinBox_general_info_rail_no_trains_per_day_freight
            spinBox_general_info_rail_no_trains_per_day_passengers
            spinBox_general_info_road_aadt_forecast
            comboBox_inspection_details_grade_crossing_type
        Related methods: 
            general_info_rail_no_trains_per_day_total
        '''
        # .valueChanged.connect(self.gcws_warrant_private_9_3_1)
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.gcws_warrant_private_9_3_1)
        self.view.spinBox_general_info_road_aadt_forecast.valueChanged.connect(self.model.gcws_warrant_private_9_3_1)
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.gcws_warrant_private_9_3_1)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.gcws_warrant_private_9_3_1)
       
        #connect signals and slots - gcws_warrant_private_9_3_2_a
        '''
        Connect input variable signals to gcws_warrant_private_9_3_2_a method slot.
        required input variables:
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_rail_no_tracks_main
            spinBox_general_info_rail_no_tracks_other
            spinBox_general_info_rail_no_trains_per_day_freight
            spinBox_general_info_rail_no_trains_per_day_passengers
            spinBox_general_info_road_aadt_forecast
            comboBox_inspection_details_grade_crossing_type
        Related methods:
            general_info_rail_no_tracks_total
            general_info_rail_no_trains_per_day_total
            general_info_rail_railway_design_speed
        '''
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.gcws_warrant_private_9_3_2_a)
        self.view.spinBox_general_info_road_aadt_forecast.valueChanged.connect(self.model.gcws_warrant_private_9_3_2_a)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.gcws_warrant_private_9_3_2_a)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.gcws_warrant_private_9_3_2_a)        
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.gcws_warrant_private_9_3_2_a)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.gcws_warrant_private_9_3_2_a)
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.gcws_warrant_private_9_3_2_a)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.gcws_warrant_private_9_3_2_a)
        
        #connect signals and slots - gcws_warrant_private_9_3_2_b
        '''
        Connect input variable signals to gcws_warrant_private_9_3_2_b method slot.
        required input variables:
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_rail_no_trains_per_day_freight
            spinBox_general_info_rail_no_trains_per_day_passengers
            spinBox_general_info_road_aadt_forecast
            comboBox_general_info_road_sidewalks
            comboBox_inspection_details_grade_crossing_type
        Related methods: 
            general_info_rail_no_trains_per_day_total
            general_info_rail_railway_design_speed
        '''
        self.view.comboBox_general_info_road_sidewalks.currentTextChanged.connect(self.model.gcws_warrant_private_9_3_2_b)
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.gcws_warrant_private_9_3_2_b)
        self.view.spinBox_general_info_road_aadt_forecast.valueChanged.connect(self.model.gcws_warrant_private_9_3_2_b)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.gcws_warrant_private_9_3_2_b)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.gcws_warrant_private_9_3_2_b)
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.gcws_warrant_private_9_3_2_b)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.gcws_warrant_private_9_3_2_b)

        #connect signals and slots - gcws_warrant_private_9_3_2_c
        '''
        Connect input variable signals to gcws_warrant_private_9_3_2_c method slot.
        required input variables:
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            comboBox_general_info_road_sidewalks
            comboBox_inspection_details_grade_crossing_type
        Related methods: 
            general_info_rail_railway_design_speed
        '''
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.gcws_warrant_private_9_3_2_c)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.gcws_warrant_private_9_3_2_c)
        self.view.comboBox_general_info_road_sidewalks.currentTextChanged.connect(self.model.gcws_warrant_private_9_3_2_c)
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.gcws_warrant_private_9_3_2_c)
        
        #TODO
        #connect signals and slots - gcws_warrant_public_9_1
        # .valueChanged.connect(self.gcws_warrant_public_9_1)

        #connect signals and slots - gcws_warrant_public_9_1_a
        '''
        Connect input variable signals to gcws_warrant_public_9_1_a method slot.
        required input variables:
            spinBox_general_info_rail_no_trains_per_day_freight
            spinBox_general_info_rail_no_trains_per_day_passengers
            spinBox_general_info_road_aadt_forecast
            comboBox_inspection_details_grade_crossing_type
        Related methods: 
            general_info_rail_no_trains_per_day_total
        '''
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.gcws_warrant_public_9_1_a)
        self.view.spinBox_general_info_road_aadt_forecast.valueChanged.connect(self.model.gcws_warrant_public_9_1_a)
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.gcws_warrant_public_9_1_a)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.gcws_warrant_public_9_1_a)
       
        #connect signals and slots - gcws_warrant_public_9_1_b
        '''
        Connect input variable signals to gcws_warrant_public_9_1_b method slot.
        required input variables:
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            comboBox_general_info_road_sidewalks
            comboBox_inspection_details_grade_crossing_type
        Related methods: 
            general_info_rail_railway_design_speed
        '''
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.gcws_warrant_public_9_1_b)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.gcws_warrant_public_9_1_b)
        self.view.comboBox_general_info_road_sidewalks.currentTextChanged.connect(self.model.gcws_warrant_public_9_1_b)
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.gcws_warrant_public_9_1_b)
  
        #connect signals and slots - gcws_warrant_public_9_1_c
        '''
        Connect input variable signals to gcws_warrant_public_9_1_c method slot.
        required input variables:
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            comboBox_general_info_road_sidewalks
            comboBox_inspection_details_grade_crossing_type
        Related methods: 
            general_info_rail_railway_design_speed
        '''
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.gcws_warrant_public_9_1_c)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.gcws_warrant_public_9_1_c)
        self.view.comboBox_general_info_road_sidewalks.currentTextChanged.connect(self.model.gcws_warrant_public_9_1_c)
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.gcws_warrant_public_9_1_c)
  
        #connect signals and slots - gcws_warrant_public_9_1_d_i
        '''
        Connect input variable signals to gcws_warrant_public_9_1_d_i method slot.
        required input variables:
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_rail_no_tracks_main
            spinBox_general_info_rail_no_tracks_other
            comboBox_inspection_details_grade_crossing_type
        Related methods:
            general_info_rail_no_tracks_total
            general_info_rail_railway_design_speed
        '''
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.gcws_warrant_public_9_1_d_i)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.gcws_warrant_public_9_1_d_i)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.gcws_warrant_public_9_1_d_i)        
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.gcws_warrant_public_9_1_d_i)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.gcws_warrant_public_9_1_d_i)
        
        #connect signals and slots - gcws_warrant_public_9_1_d_ii
        '''
        Connect input variable signals to gcws_warrant_public_9_1_d_ii method slot.
        required input variables:
            comboBox_inspection_details_grade_crossing_type
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_or_w_approach
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
        Related methods:
            general_info_rail_railway_design_speed
        '''
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.gcws_warrant_public_9_1_d_ii)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach.valueChanged.connect(self.model.gcws_warrant_public_9_1_d_ii)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_or_w_approach.valueChanged.connect(self.model.gcws_warrant_public_9_1_d_ii)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.gcws_warrant_public_9_1_d_ii)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.gcws_warrant_public_9_1_d_ii)        
        
        #connect signals and slots - gcws_warrant_public_9_1_d_iii
        '''
        Connect input variable signals to gcws_warrant_public_9_1_d_iii method slot.
        required input variables:
            comboBox_inspection_details_grade_crossing_type
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
        Related methods:
            general_info_rail_railway_design_speed
        '''
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.gcws_warrant_public_9_1_d_iii)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach.valueChanged.connect(self.model.gcws_warrant_public_9_1_d_iii)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach.valueChanged.connect(self.model.gcws_warrant_public_9_1_d_iii)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.gcws_warrant_public_9_1_d_iii)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.gcws_warrant_public_9_1_d_iii)        
        
        #connect signals and slots - gcws_warrant_sidewalk_9_5
        #TODO add design vehcile pedestrian
        '''
        Connect input variable signals to gcws_warrant_sidewalk_9_5 method slot.
        required input variables:
            comboBox_general_info_road_sidewalks
            comboBox_general_info_road_sidewalk_island_circuit
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
        Related methods:
            general_info_rail_railway_design_speed
        '''
        # .valueChanged.connect(self.gcws_warrant_sidewalk_9_5)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.gcws_warrant_sidewalk_9_5)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.gcws_warrant_sidewalk_9_5)        
        self.view.comboBox_general_info_road_sidewalks.currentTextChanged.connect(self.model.gcws_warrant_sidewalk_9_5)   
        self.view.comboBox_general_info_road_sidewalk_island_circuit.currentTextChanged.connect(self.model.gcws_warrant_sidewalk_9_5)   

        #TODO
        #connect signals and slots - gates_gcws_warrant_private_9_4_1_a
        '''
        Connect input variable signals to gates_gcws_warrant_private_9_4_1_a method slot.
        required input variables:
            gcws private warrants
            comboBox_inspection_details_grade_crossing_type
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_rail_no_tracks_main
            spinBox_general_info_rail_no_tracks_other
            spinBox_general_info_rail_no_trains_per_day_freight
            spinBox_general_info_rail_no_trains_per_day_passengers
            spinBox_general_info_road_aadt_forecast
            comboBox_general_info_road_sidewalks    
        Related methods:           
            gcws private warrants
            gcws_warrant_private_9_3_1
            gcws_warrant_private_9_3_2_a
            gcws_warrant_private_9_3_2_b
            gcws_warrant_private_9_3_2_c
            general_info_rail_no_tracks_total
            general_info_rail_no_trains_per_day_total
            general_info_rail_railway_design_speed    
        '''
        #gcws private warrants
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_a)
        self.view.comboBox_general_info_road_sidewalks.currentTextChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_a)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_a)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_a)        
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_a)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_a)
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_a)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_a)
        self.view.spinBox_general_info_road_aadt_forecast.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_a)

        #TODO
        #connect signals and slots - gates_gcws_warrant_private_9_4_1_b
        '''
        Connect input variable signals to gates_gcws_warrant_private_9_4_1_b method slot.
        required input variables:
            gcws private warrants
            comboBox_inspection_details_grade_crossing_type
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_rail_no_tracks_main
            spinBox_general_info_rail_no_tracks_other
            spinBox_general_info_rail_no_trains_per_day_freight
            spinBox_general_info_rail_no_trains_per_day_passengers
            spinBox_general_info_road_aadt_forecast
            comboBox_general_info_road_sidewalks    
        Related methods:           
            gcws private warrants
            gcws_warrant_private_9_3_1
            gcws_warrant_private_9_3_2_a
            gcws_warrant_private_9_3_2_b
            gcws_warrant_private_9_3_2_c
            general_info_rail_no_tracks_total
            general_info_rail_no_trains_per_day_total
            general_info_rail_railway_design_speed    
        '''
        #gcws private warrants
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_b)
        self.view.comboBox_general_info_road_sidewalks.currentTextChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_b)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_b)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_b)        
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_b)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_b)
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_b)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_b)
        self.view.spinBox_general_info_road_aadt_forecast.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_b)

        #TODO
        #connect signals and slots - gates_gcws_warrant_private_9_4_1_c
        '''
        Connect input variable signals to gates_gcws_warrant_private_9_4_1_c method slot.
        required input variables:
            gcws private warrants
            comboBox_inspection_details_grade_crossing_type
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_rail_no_tracks_main
            spinBox_general_info_rail_no_tracks_other
            spinBox_general_info_rail_no_trains_per_day_freight
            spinBox_general_info_rail_no_trains_per_day_passengers
            spinBox_general_info_road_aadt_forecast
            comboBox_general_info_road_sidewalks    
        Related methods:           
            gcws private warrants
            gcws_warrant_private_9_3_1
            gcws_warrant_private_9_3_2_a
            gcws_warrant_private_9_3_2_b
            gcws_warrant_private_9_3_2_c
            general_info_rail_no_tracks_total
            general_info_rail_no_trains_per_day_total
            general_info_rail_railway_design_speed    
        '''
        #gcws private warrants
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_c)
        self.view.comboBox_general_info_road_sidewalks.currentTextChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_c)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_c)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_c)        
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_c)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_c)
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_c)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_c)
        self.view.spinBox_general_info_road_aadt_forecast.valueChanged.connect(self.model.gates_gcws_warrant_private_9_4_1_c)

        #TODO
        #connect signals and slots - gates_gcws_warrant_public_9_2_1_a
        '''
        Connect input variable signals to gates_gcws_warrant_public_9_2_1_a method slot.
        required input variables:
            gcws Public warrants
            comboBox_general_info_road_sidewalks
            comboBox_inspection_details_grade_crossing_type
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_or_w_approach
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_rail_no_tracks_main
            spinBox_general_info_rail_no_tracks_other
            spinBox_general_info_rail_no_trains_per_day_freight
            spinBox_general_info_rail_no_trains_per_day_passengers
            spinBox_general_info_road_aadt_forecast

        Related methods:
            gcws Public warrants
            gcws_warrant_public_9_1_a
            gcws_warrant_public_9_1_b
            gcws_warrant_public_9_1_c
            gcws_warrant_public_9_1_d_i
            gcws_warrant_public_9_1_d_ii
            gcws_warrant_public_9_1_d_iii
            general_info_rail_no_tracks_total
            general_info_rail_no_trains_per_day_total
            general_info_rail_railway_design_speed
        '''
        self.view.comboBox_general_info_road_sidewalks.currentTextChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_a)
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_a)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_a)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_a)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_a)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_or_w_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_a)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_a)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_a)
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_a)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_a)
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_a)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_a)
        self.view.spinBox_general_info_road_aadt_forecast.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_a)

        #TODO
        #connect signals and slots - gates_gcws_warrant_public_9_2_1_b
        '''
        Connect input variable signals to gates_gcws_warrant_public_9_2_1_b method slot.
        required input variables:
            gcws Public warrants
            comboBox_general_info_road_sidewalks
            comboBox_inspection_details_grade_crossing_type
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_or_w_approach
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_rail_no_tracks_main
            spinBox_general_info_rail_no_tracks_other
            spinBox_general_info_rail_no_trains_per_day_freight
            spinBox_general_info_rail_no_trains_per_day_passengers
            spinBox_general_info_road_aadt_forecast

        Related methods:
            gcws Public warrants
            gcws_warrant_public_9_1_a
            gcws_warrant_public_9_1_b
            gcws_warrant_public_9_1_c
            gcws_warrant_public_9_1_d_i
            gcws_warrant_public_9_1_d_ii
            gcws_warrant_public_9_1_d_iii
            general_info_rail_no_tracks_total
            general_info_rail_no_trains_per_day_total
            general_info_rail_railway_design_speed
        '''
        self.view.comboBox_general_info_road_sidewalks.currentTextChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_b)
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_b)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_b)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_b)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_b)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_or_w_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_b)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_b)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_b)
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_b)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_b)
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_b)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_b)
        self.view.spinBox_general_info_road_aadt_forecast.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_b)

        #TODO
        #connect signals and slots - gates_gcws_warrant_public_9_2_1_c
        '''
        Connect input variable signals to gates_gcws_warrant_public_9_2_1_c method slot.
        required input variables:
            gcws Public warrants
            comboBox_general_info_road_sidewalks
            comboBox_inspection_details_grade_crossing_type
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_or_w_approach
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_rail_no_tracks_main
            spinBox_general_info_rail_no_tracks_other
            spinBox_general_info_rail_no_trains_per_day_freight
            spinBox_general_info_rail_no_trains_per_day_passengers
            spinBox_general_info_road_aadt_forecast

        Related methods:
            gcws Public warrants
            gcws_warrant_public_9_1_a
            gcws_warrant_public_9_1_b
            gcws_warrant_public_9_1_c
            gcws_warrant_public_9_1_d_i
            gcws_warrant_public_9_1_d_ii
            gcws_warrant_public_9_1_d_iii
            general_info_rail_no_tracks_total
            general_info_rail_no_trains_per_day_total
            general_info_rail_railway_design_speed
        '''
        self.view.comboBox_general_info_road_sidewalks.currentTextChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_c)
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_c)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_c)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_c)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_c)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_or_w_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_c)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_c)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_c)
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_c)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_c)
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_c)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_c)
        self.view.spinBox_general_info_road_aadt_forecast.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_c)

        #TODO
        #connect signals and slots - gates_gcws_warrant_public_9_2_1_d
        '''
        Connect input variable signals to gates_gcws_warrant_public_9_2_1_d method slot.
        required input variables:
            gcws Public warrants
            comboBox_general_info_road_sidewalks
            comboBox_inspection_details_grade_crossing_type
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_or_w_approach
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_rail_no_tracks_main
            spinBox_general_info_rail_no_tracks_other
            spinBox_general_info_rail_no_trains_per_day_freight
            spinBox_general_info_rail_no_trains_per_day_passengers
            spinBox_general_info_road_aadt_forecast

        Related methods:
            gcws Public warrants
            gcws_warrant_public_9_1_a
            gcws_warrant_public_9_1_b
            gcws_warrant_public_9_1_c
            gcws_warrant_public_9_1_d_i
            gcws_warrant_public_9_1_d_ii
            gcws_warrant_public_9_1_d_iii
            general_info_rail_no_tracks_total
            general_info_rail_no_trains_per_day_total
            general_info_rail_railway_design_speed
        '''
        self.view.comboBox_general_info_road_sidewalks.currentTextChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_d)
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_d)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_d)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_d)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_d)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_or_w_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_d)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_d)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_d)
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_d)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_d)
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_d)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_d)
        self.view.spinBox_general_info_road_aadt_forecast.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_d)

        #TODO
        # connect signals and slots - gates_gcws_warrant_public_9_2_1_e
        '''
        Connect input variable signals to gates_gcws_warrant_public_9_2_1_e method slot.
        required input variables:
            gcws Public warrants
            comboBox_general_info_road_sidewalks
            comboBox_inspection_details_grade_crossing_type
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_or_w_approach
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_rail_no_tracks_main
            spinBox_general_info_rail_no_tracks_other
            spinBox_general_info_rail_no_trains_per_day_freight
            spinBox_general_info_rail_no_trains_per_day_passengers
            spinBox_general_info_road_aadt_forecast

        Related methods:
            gcws Public warrants
            gcws_warrant_public_9_1_a
            gcws_warrant_public_9_1_b
            gcws_warrant_public_9_1_c
            gcws_warrant_public_9_1_d_i
            gcws_warrant_public_9_1_d_ii
            gcws_warrant_public_9_1_d_iii
            general_info_rail_no_tracks_total
            general_info_rail_no_trains_per_day_total
            general_info_rail_railway_design_speed
        '''
        self.view.comboBox_general_info_road_sidewalks.currentTextChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_e)
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_e)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_e)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_e)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_e)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_or_w_approach.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_e)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_e)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_e)
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_e)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_e)
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_e)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_e)
        self.view.spinBox_general_info_road_aadt_forecast.valueChanged.connect(self.model.gates_gcws_warrant_public_9_2_1_e)

        #TODO
        #connect signals and slots - gates_gcws_warrant_sidewalk_9_6
        '''
        Connect input variable signals to gates_gcws_warrant_sidewalk_9_6 method slot.
        required input variables:
            comboBox_general_info_road_sidewalks 
            comboBox_general_info_road_sidewalk_island_circuit
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_rail_no_tracks_main
            spinBox_general_info_rail_no_tracks_other
        Related methods:
            general_info_rail_railway_design_speed
            general_info_rail_no_tracks_total
        '''
        self.view.comboBox_general_info_road_sidewalks.currentTextChanged.connect(self.model.gates_gcws_warrant_sidewalk_9_6)
        self.view.comboBox_general_info_road_sidewalk_island_circuit.currentTextChanged.connect(self.model.gates_gcws_warrant_sidewalk_9_6)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.gates_gcws_warrant_sidewalk_9_6)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.gates_gcws_warrant_sidewalk_9_6)
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.gates_gcws_warrant_sidewalk_9_6)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.gates_gcws_warrant_sidewalk_9_6)

        #grade CROSSING warnING systEMS (GCS seCTION 12-16)
        #TODO
        #connect signals and slots - gcws_rail_design_warning_time_adjacent_crossing
        # .valueChanged.connect(self.gcws_rail_design_warning_time_adjacent_crossing)
        
        #TODO includes pedestrian clearance
        #connect signals and slots - gcws_rail_design_warning_time_clearance_distance
        '''
        Connect input variable signals to gcws_rail_design_warning_time_clearance_distance method slot.
        required input variables:
            comboBox_design_road_design_vehicle_type
            doubleSpinBox_design_measture_clearance_distance_pedestrian
            doubleSpinBox_design_measture_clearance_distance_vehicle 
        Related methods:
            none
        '''
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.gcws_rail_design_warning_time_clearance_distance)
        self.view.doubleSpinBox_design_measture_clearance_distance_pedestrian.valueChanged.connect(self.model.gcws_rail_design_warning_time_clearance_distance)
        self.view.doubleSpinBox_design_measture_clearance_distance_vehicle.valueChanged.connect(self.model.gcws_rail_design_warning_time_clearance_distance)
        
        #connect signals and slots - gcws_rail_design_warning_time_departure_time_vehicle
        '''
        Connect input variable signals to gcws_rail_design_warning_time_departure_time_vehicle method slot.
        required input variables:
            doubleSpinBox_design_measture_clearance_distance_pedestrian
            doubleSpinBox_design_measture_clearance_distance_vehicle
            doubleSpinBox_design_road_max_approach_grade_within_s
            combo_Box_design_road_design_vehicle_type        
        Related methods:
            design_calculate_clearance_time_vehicle_design_check
            design_input_reaction_time
            design_calculate_vehicle_departure_time_grade_adjusted
            design_calculate_vehicle_departure_time
            design_calculate_vehicle_travel_distance
            design_lookup_design_vehicle_length
            design_lookup_design_vehicle_class
            design_lookup_grade_adjustment_factor
        '''
        self.view.doubleSpinBox_design_measture_clearance_distance_pedestrian.valueChanged.connect(self.model.gcws_rail_design_warning_time_departure_time_vehicle)
        self.view.doubleSpinBox_design_measture_clearance_distance_vehicle.valueChanged.connect(self.model.gcws_rail_design_warning_time_departure_time_vehicle)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.gcws_rail_design_warning_time_departure_time_vehicle)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.gcws_rail_design_warning_time_departure_time_vehicle)

        #connect signals and slots - gcws_rail_design_warning_time_departure_time_pedestrian
        '''
        Connect input variable signals to gcws_rail_design_warning_time_departure_time_pedestrian method slot.
        required input variables:
            doubleSpinBox_design_measture_clearance_distance_pedestrian
        Related methods:
            self.model.design_calculate_clearance_time_pedestrian_design_check
        '''
        self.view.doubleSpinBox_design_measture_clearance_distance_pedestrian.valueChanged.connect(self.model.gcws_rail_design_warning_time_departure_time_pedestrian)

        #connect signals and slots - gcws_rail_design_warning_time_gate_arm_clearance
        '''
        Connect input variable signals to gcws_rail_design_warning_time_gate_arm_clearance method slot.
        required input variables:
            spinBox_general_info_road_speed_design
            doubleSpinBox_design_road_max_approach_grade_within_s
            doubleSpinBox_gates_gcws_rail_gate_arm_descent_time_design
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach
            comboBox_design_road_design_vehicle_type
        Related methods:
            label_design_input_reaction_time
            design_calculate_gate_arm_clearance_time_vehicle_recommended
            design_calculate_gate_arm_clearance_time_vehicle_ssd
            design_lookup_design_vehicle_class
            design_lookup_design_vehicle_length
            sightlines_lookup_ssd_minimum_n_or_e_approach
            sightlines_lookup_ssd_minimum_s_or_w_approach
            design_calculate_gate_arm_clearance_time_vehicle_stop
            design_lookup_grade_adjustment_factor
            design_calculate_vehicle_departure_time_gate_arm_clearance
        '''
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.gcws_rail_design_warning_time_gate_arm_clearance)
        #TODO Remove pedestrian clearance distance
        # self.view.doubleSpinBox_design_measture_clearance_distance_pedestrian.valueChanged.connect(self.model.gcws_rail_design_warning_time_gate_arm_clearance('doubleSpinBox_design_measture_clearance_distance_pedestrian', val))
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.gcws_rail_design_warning_time_gate_arm_clearance)
        self.view.doubleSpinBox_gates_gcws_rail_gate_arm_descent_time_design.valueChanged.connect(self.model.gcws_rail_design_warning_time_gate_arm_clearance)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.gcws_rail_design_warning_time_gate_arm_clearance)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.gcws_rail_design_warning_time_gate_arm_clearance)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.gcws_rail_design_warning_time_gate_arm_clearance)
        
        #TODO
        #connect signals and slots - gcws_rail_design_warning_time_preemption
        # .valueChanged.connect(self.gcws_rail_design_warning_time_preemption)
        
        #connect signals and slots - gcws_rail_design_warning_time_ssd
        '''
        Connect input variable signals to gcws_rail_design_warning_time_ssd method slot.
        required input variables:
            spinBox_general_info_road_speed_design
            doubleSpinBox_design_measture_clearance_distance_vehicle
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach
            comboBox_design_road_design_vehicle_type
        Related methods:
            design_calculate_vehicle_travel_distance
            design_lookup_design_vehicle_class
            design_lookup_design_vehicle_length
            sightlines_lookup_ssd_minimum_n_or_e_approach
            sightlines_lookup_ssd_minimum_s_or_w_approach
        '''
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.gcws_rail_design_warning_time_ssd)
        self.view.doubleSpinBox_design_measture_clearance_distance_vehicle.valueChanged.connect(self.model.gcws_rail_design_warning_time_ssd)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.gcws_rail_design_warning_time_ssd)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.gcws_rail_design_warning_time_ssd)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.gcws_rail_design_warning_time_ssd)

        #TODO
        # connect signals and slots - gcws_rail_design_approach_warning_time
        # .valueChanged.connect(self.gcws_rail_design_approach_warning_time)
        
        # gateS for grade CROSSING warnING systEMS (GCS seCTION 10, 12, 15)
        
        #TODO
        #connect signals and slots - gates_gcws_calculate_inner_gate_arm_delay_time_recommended
        '''
        Connect input variable signals to gates_gcws_calculate_inner_gate_arm_delay_time_recommended method slot.
        required input variables: 
            doubleSpinBox_design_measture_adjacent_track_separation_distance, doubleSpinBox_design_measture_adjacent_track_clearance_distance
        Related methods:
            none
        '''
        self.view.doubleSpinBox_design_measture_adjacent_track_separation_distance.valueChanged.connect(self.model.gates_gcws_calculate_inner_gate_arm_delay_time_recommended)
        self.view.doubleSpinBox_design_measture_adjacent_track_clearance_distance.valueChanged.connect(self.model.gates_gcws_calculate_inner_gate_arm_delay_time_recommended)

        # PREPARE TO stop AT railWAY CROSSING sign (GCS seCTION 18)
        #TODO
        #connect signals and slots - aawd_calculate_advance_activation_time_design_n_or_e_approach
        '''
        Connect input variable signals to aawd_calculate_advance_activation_time_design_n_or_e_approach method slot.
        required input variables:
            spinBox_general_info_road_speed_design
            doubleSpinBox_design_measture_clearance_distance_vehicle
            comboBox_design_road_design_vehicle_type
            spinBox_general_info_road_speed_posted
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach  
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach  
        Related methods:
            design_calculate_vehicle_travel_distance
            design_lookup_design_vehicle_length
            aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended
            label_design_input_reaction_time
        '''
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.aawd_calculate_advance_activation_time_design_n_or_e_approach)
        self.view.doubleSpinBox_design_measture_clearance_distance_vehicle.valueChanged.connect(self.model.aawd_calculate_advance_activation_time_design_n_or_e_approach)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.aawd_calculate_advance_activation_time_design_n_or_e_approach)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.aawd_calculate_advance_activation_time_design_n_or_e_approach)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.aawd_calculate_advance_activation_time_design_n_or_e_approach)
        
        #TODO
        #connect signals and slots - aawd_calculate_advance_activation_time_design_s_or_w_approach
        '''
        Connect input variable signals to aawd_calculate_advance_activation_time_design_s_or_w_approach method slot.
        required input variables:
            spinBox_general_info_road_speed_design
            doubleSpinBox_design_measture_clearance_distance_vehicle
            comboBox_design_road_design_vehicle_type
            spinBox_general_info_road_speed_posted
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach  
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach  
        Related methods:
            design_calculate_vehicle_travel_distance
            design_lookup_design_vehicle_length
            aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended
            label_design_input_reaction_time
        '''
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.aawd_calculate_advance_activation_time_design_s_or_w_approach)
        self.view.doubleSpinBox_design_measture_clearance_distance_vehicle.valueChanged.connect(self.model.aawd_calculate_advance_activation_time_design_s_or_w_approach)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.aawd_calculate_advance_activation_time_design_s_or_w_approach)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.aawd_calculate_advance_activation_time_design_s_or_w_approach)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.aawd_calculate_advance_activation_time_design_s_or_w_approach)

        #TODO
        #connect signals and slots - aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended
        '''
        Connect input variable signals to aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended method slot.
        required input variables:
            spinBox_general_info_road_speed_posted
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach
        Related methods:
            label_design_input_reaction_time
        '''
        self.view.spinBox_general_info_road_speed_posted.valueChanged.connect(self.model.aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended)  
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended)  

        #TODO
        #connect signals and slots - aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended
        '''
        Connect input variable signals to aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended method slot.
        required input variables:
            spinBox_general_info_road_speed_posted
            doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach
            doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach
        Related methods:
            label_design_input_reaction_time
        '''
        self.view.spinBox_general_info_road_speed_posted.valueChanged.connect(self.model.aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended)  
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended)

        #TODO
        #connect signals and slots - aawd_warrant_gcr_lookup_road_classification
        '''
        Connect input variable signals to aawd_warrant_gcr_lookup_road_classification method slot.
        required input variables:
            comboBox_general_info_road_classification
        Related methods:
            none
        '''
        self.view.comboBox_general_info_road_classification.currentTextChanged.connect(self.model.aawd_warrant_gcr_lookup_road_classification)

        #connect signals and slots - aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr
        '''
        Connect input variable signals to aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr method slot.
        required input variables:
            spinBox_general_info_road_speed_design
        required methods:
            none
        '''
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr)
        
        # interCONneCTION OF traFFIC signALS (GCS seCTION 19)
        #connect signals and slots - preemption_of_traffic_signals_lookup_proximity_condition
        '''
        Connect input variable signals to preemption_of_traffic_signals_lookup_proximity_condition method slot.
        required input variables:
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach
        required methods:
            none
        '''
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach.valueChanged.connect(self.model.preemption_of_traffic_signals_lookup_proximity_condition)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach.valueChanged.connect(self.model.preemption_of_traffic_signals_lookup_proximity_condition)

        #connect signals and slots - preemption_of_traffic_signals_lookup_required
        '''
        Connect input variable signals to preemption_of_traffic_signals_lookup_required method slot.
        required input variables:
            spinBox_general_info_rail_max_railway_operating_speed_freight 
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach
        required methods:
            preemption_of_traffic_signals_lookup_proximity_condition
            general_info_rail_railway_design_speed
        '''
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.preemption_of_traffic_signals_lookup_required)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.preemption_of_traffic_signals_lookup_required)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach.valueChanged.connect(self.model.preemption_of_traffic_signals_lookup_required)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach.valueChanged.connect(self.model.preemption_of_traffic_signals_lookup_required)

        # whistLE CESSATION (GCS seCTION Appendix D)
        #TODO
        #connect signals and slots - areast_without_train_whistling_lookup_gcs_9_2
        '''
        Connect input variable signals to areast_without_train_whistling_lookup_gcs_9_2 method slot.
        required input variables:
            comboBox_gcws_observe_gates_n_or_e_approach
            comboBox_gcws_observe_gates_s_or_w_approach
            gcws Public warrants
            comboBox_general_info_road_sidewalks
            comboBox_inspection_details_grade_crossing_type
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_or_w_approach
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_rail_no_tracks_main
            spinBox_general_info_rail_no_tracks_other
            spinBox_general_info_rail_no_trains_per_day_freight
            spinBox_general_info_rail_no_trains_per_day_passengers
            spinBox_general_info_road_aadt_forecast
        required methods:
            gcws Public warrants
            gcws_warrant_public_9_1_a
            gcws_warrant_public_9_1_b
            gcws_warrant_public_9_1_c
            gcws_warrant_public_9_1_d_i
            gcws_warrant_public_9_1_d_ii
            gcws_warrant_public_9_1_d_iii
            general_info_rail_no_tracks_total
            general_info_rail_no_trains_per_day_total
            general_info_rail_railway_design_speed        
            '''
        self.view.comboBox_gcws_observe_gates_n_or_e_approach.currentTextChanged.connect(self.model.areast_without_train_whistling_lookup_gcs_9_2)
        self.view.comboBox_gcws_observe_gates_s_or_w_approach.currentTextChanged.connect(self.model.areast_without_train_whistling_lookup_gcs_9_2)
        self.view.comboBox_general_info_road_sidewalks.currentTextChanged.connect(self.model.areast_without_train_whistling_lookup_gcs_9_2)
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.areast_without_train_whistling_lookup_gcs_9_2)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach.valueChanged.connect(self.model.areast_without_train_whistling_lookup_gcs_9_2)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach.valueChanged.connect(self.model.areast_without_train_whistling_lookup_gcs_9_2)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach.valueChanged.connect(self.model.areast_without_train_whistling_lookup_gcs_9_2)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_or_w_approach.valueChanged.connect(self.model.areast_without_train_whistling_lookup_gcs_9_2)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.areast_without_train_whistling_lookup_gcs_9_2)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.areast_without_train_whistling_lookup_gcs_9_2)
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.areast_without_train_whistling_lookup_gcs_9_2)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.areast_without_train_whistling_lookup_gcs_9_2)
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.areast_without_train_whistling_lookup_gcs_9_2)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.areast_without_train_whistling_lookup_gcs_9_2)
        self.view.spinBox_general_info_road_aadt_forecast.valueChanged.connect(self.model.areast_without_train_whistling_lookup_gcs_9_2)

        #connect signals and slots - areast_without_train_whistling_requirements_lookup_table_d1_criteria
        '''
        Connect input variable signals to areast_without_train_whistling_requirements_lookup_table_d1_criteria method slot.
        required input variables:
            spinBox_general_info_rail_no_tracks_main
            spinBox_general_info_rail_no_tracks_other
            spinBox_general_info_rail_max_railway_operating_speed_freight 
            spinBox_general_info_rail_max_railway_operating_speed_passenger
        required methods:
            general_info_rail_no_tracks_total
            general_info_rail_railway_design_speed
        '''
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.areast_without_train_whistling_requirements_lookup_table_d1_criteria)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.areast_without_train_whistling_requirements_lookup_table_d1_criteria)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.areast_without_train_whistling_requirements_lookup_table_d1_criteria)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.areast_without_train_whistling_requirements_lookup_table_d1_criteria)

        #connect signals and slots - areast_without_train_whistling_requirements_observe_table_d1
        '''
        Connect input variable signals to areast_without_train_whistling_requirements_observe_table_d1 method slot.
        required input variables:
            comboBox_gcws_observe_gates_n_or_e_approach
            comboBox_gcws_observe_gates_s_or_w_approach
            comboBox_gcws_observe_light_units_n_or_e_approach
            comboBox_gcws_observe_light_units_s_or_w_approach
            spinBox_general_info_rail_no_tracks_main
            spinBox_general_info_rail_no_tracks_other
            spinBox_general_info_rail_max_railway_operating_speed_freight 
            spinBox_general_info_rail_max_railway_operating_speed_passenger
        required methods:
            areast_without_train_whistling_requirements_lookup_table_d1_criteria
            general_info_rail_no_tracks_total
            general_info_rail_railway_design_speed
        '''
        self.view.comboBox_gcws_observe_gates_n_or_e_approach.currentTextChanged.connect(self.model.areast_without_train_whistling_requirements_observe_table_D1)
        self.view.comboBox_gcws_observe_gates_s_or_w_approach.currentTextChanged.connect(self.model.areast_without_train_whistling_requirements_observe_table_D1)
        self.view.comboBox_gcws_observe_light_units_n_or_e_approach.currentTextChanged.connect(self.model.areast_without_train_whistling_requirements_observe_table_D1)
        self.view.comboBox_gcws_observe_light_units_s_or_w_approach.currentTextChanged.connect(self.model.areast_without_train_whistling_requirements_observe_table_D1)
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.areast_without_train_whistling_requirements_observe_table_D1)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.areast_without_train_whistling_requirements_observe_table_D1)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.areast_without_train_whistling_requirements_observe_table_D1) 
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.areast_without_train_whistling_requirements_observe_table_D1)

    def map_fields_to_sql(self):
    # Map the crossing fields
        self.mapper = qtw.QdataWidgetMapper(self)
        self.mapper.setModel(self.db.db_model_crossing_assessment_ca)
        self.mapper.setItemDelegate(
            qts.QSqlRelationalDelegate(self))
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('functional_location')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('aawd_calculate_aawd_advance_activation_time_design_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('aawd_calculate_aawd_advance_activation_time_design_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('aawd_measture_distance_between_sign_and_stopline_n_or_e_approach_actual')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('aawd_measture_distance_between_sign_and_stopline_n_or_e_approach_recommended')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('aawd_measture_distance_between_sign_and_stopline_s_or_w_approach_actual')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('aawd_measture_distance_between_sign_and_stopline_s_or_w_approach_recommended')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('aawd_observe_present_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('aawd_observe_present_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('aawd_rail_aawd_advance_activation_time_actual_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('aawd_rail_aawd_advance_activation_time_actual_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('aawd_road_aawd_advance_activation_time_info_sharing')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('aawd_road_aawd_operation_time')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('aawd_warrant_gcr_lookup_road_classification')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('aawd_warrant_gcr_observe_environmental_condition')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('aawd_warrant_gcr_observe_sightline_obstruction')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('aawd_warrant_mutcd_lookup_significant_road_downgrade')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('areast_Whithout_train_whistling_observe_trespassing_area')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('areast_without_train_whistling_rail_anti_whistling_zone')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('areast_without_train_whistling_requirements_lookup_GCS_12_16')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('areast_without_train_whistling_requirements_lookup_GCS_9_2')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('areast_without_train_whistling_requirements_observe_for_stop_and_proceed')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('collision_history_comments')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('collision_history_fatal_injury')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('collision_history_fatalities')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('collision_history_personal_injuries')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('collision_history_personal_injury')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('collision_history_property_damage')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('collision_history_total_5_year_period')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_calculate_adjacent_track_clearance_time')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_calculate_clearance_time_crossing_pedestrian_design_check')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_calculate_clearance_time_crossing_vehicle_design_check')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_calculate_clearance_time_gate_arm_ssd')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_calculate_clearance_time_gate_arm_stop')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_calculate_vehicle_travel_distance')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_input_reaction_time')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_lookup_design_vehicle_Class')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_lookup_design_vehicle_length')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_lookup_grade_adjustment_Factor')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_lookup_vehicle_departure_time_Crossing')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_lookup_vehicle_departure_time_gate_arm_clearance')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_measture_adjacent_track_clearance_distance')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_measture_adjacent_track_separation_distance')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_measture_clearance_distance_crossing_pedestrian')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_measture_clearance_distance_crossing_vehicle')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_measture_clearance_distance_gate_arm_ssd')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_measture_clearance_distance_gate_arm_stop')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_observe_field_acceleration_times_exceed_td')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_observe_k_factor_crossing_nearby_intersection')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_observe_k_factor_crossing_surface_condition')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_observe_k_factor_other')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_observe_k_factor_pavement_marking_condition')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_observe_k_factor_superelevation')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_observe_k_factor_vehicle_restrictions')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_road_clearance_time_crossing_pedestrian_info_sharing')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_road_clearance_time_crossing_vehicle_info_sharing')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_road_design_vehicle_type')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('design_considerations_road_max_approach_grade_Within_S')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('flashing_light_units_lookup_distance_primary_lights_minimum_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('flashing_light_units_lookup_distance_primary_lights_minimum_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('flashing_light_units_measture_alignment_height_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('flashing_light_units_measture_alignment_height_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('flashing_light_units_measture_cantilever_lights_dl_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('flashing_light_units_measture_cantilever_lights_dl_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('flashing_light_units_measture_cantilever_lights_dr_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('flashing_light_units_measture_cantilever_lights_dr_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('flashing_light_units_observe_supplemental_lights_by_road_alignment_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('flashing_light_units_observe_supplemental_lights_by_road_alignment_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('flashing_light_units_observe_supplemental_lights_by_road_intersection_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('flashing_light_units_observe_supplemental_lights_by_road_intersection_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('flashing_light_units_observe_supplemental_lights_sidewalks_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('flashing_light_units_observe_supplemental_lights_sidewalks_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('flashing_light_units_observe_visibility_back_lights_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('flashing_light_units_observe_visibility_back_lights_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('flashing_light_units_observe_visibility_front_lights_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('flashing_light_units_observe_visibility_front_lights_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gates_gcws_calculate_warrant_cross_product')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gates_gcws_lookup_gate_arm_clearance_time_design')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gates_gcws_lookup_warrant_max_rail_operating_speed')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gates_gcws_lookup_warrant_sightlines')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gates_gcws_observe_gate_arm_Rest')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gates_gcws_observe_gate_ascent_time')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gates_gcws_observe_gate_descent_time')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gates_gcws_observe_warrant_proximity_condition_stop_sign')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gates_gcws_observe_warrant_proximity_condition_traffic_signal')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gates_gcws_rail_gate_arm_delay_time_actual')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gates_gcws_rail_gate_arm_descent_time')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gates_gcws_rail_inner_gate_arm_delay_time_actual')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gates_gcws_rail_warrant_no_of_tracks')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_calculate_warrant_cross_product')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_lookup_warrant_max_rail_operating_speed')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_lookup_warrant_sightlines')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_bell_If_sidewalk')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_bells')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_bells_condition')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_bells_number')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_cantilever_lights')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_cantilever_lights_condition')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_cantilever_lights_number')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_gates')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_gates_condition')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_gates_number')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_gcws_limited_Use_With_walk_light_assembly')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_gcws_limited_Use_without_walk_light_assembly')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_light_units')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_light_units_condition')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_light_units_number')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_warning_signal_assemblies')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_warning_system_Housing_location')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_warning_time_consistency')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_warning_time_consistency_Reduced_speed')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_warrant_proximity_condition_stop_sign')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_observe_warrant_proximity_condition_traffic_signal')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_rail_crossing_warning_time_actual')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_rail_cut_out_circuit_requirements')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_rail_design_approach_warning_time')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_rail_directional_stick_circuit_requirements')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_rail_equipment_reaction_time')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_rail_event_data_recorder')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_rail_foreign_railway_interconnect')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_rail_method_of_train_detection')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_rail_remote_monitoring_and_access')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_rail_self_diagnostic')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_rail_video_recorder')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('gcws_rail_warrant_no_of_tracks')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_rail_max_railway_operating_speed_freight')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_rail_max_railway_operating_speed_passenger')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_rail_railway_design_speed')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_rail_no_tracks_main')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_rail_no_tracks_other')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_rail_no_tracks_total')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_rail_no_trains_per_day_freights')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_rail_no_trains_per_day_passenger')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_rail_no_trains_per_day_total')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_aadt_current')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_aadt_forecasted')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_aadt_year_current')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_aadt_year_forecasted')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_assistive_pedestrian_devices')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_bicycle_lane_n_or_e_side')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_bicycle_lane_s_or_w_side')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_classification')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_cyclist_per_day')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_no_traffic_lanes_bidirectional')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_no_traffic_lanes_northbound_or_easttbound')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_no_traffic_lanes_southbound_or_westbound')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_no_traffic_lanes_total')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_pedestrians_per_day')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_sidewalk_n_or_e_side')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_sidewalk_s_or_w_side')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_speed_design')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_speed_posted')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_sub_classification')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_road_traffic_median')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('general_info_train_switching')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_crossing_surface_extension_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_crossing_surface_extension_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_crossing_surface_length')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_distance_between_signal_mast_and_sidewalk_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_distance_between_signal_mast_and_sidewalk_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_elevation_top_of_rail_above_road_surface')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_elevation_top_of_rail_below_road_surface')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_flangeway_depth')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_flangeway_width')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_road_surface_Median_width')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_road_surface_shoulder_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_road_surface_shoulder_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_road_surface_travel_lanes_width_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_road_surface_travel_lanes_width_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_side_grinding_depth')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_side_grinding_width')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_sidewalk_extension_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_sidewalk_extension_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_sidewalk_width_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_measture_sidewalk_width_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_observe_road_approach_surface_condition')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_observe_road_approach_surface_type')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_observe_crossing_smoothness')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_observe_crossing_surface_condition')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('grade_crossing_surface_observe_Material')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_assessment_Team')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_Country')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_crossing_location')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_crossing_status')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_Date_assessment')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_functional_location')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_gcws_type')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_grade_crossing_type')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_latitude')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_longitude')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_location_reference')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_mile')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_municipality')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_private_crossing_use')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_province')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_railway_authority')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_railway_operators')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_reason_for_assessment')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_road_authority')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_road_name')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_road_number')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_seniority')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_spur_mile')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_spur_name')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_subdivision_mile')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_subdivision_name')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_tc_crossing_number')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_track_ID')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('inspection_details_track_type')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('location_of_grade_crossing_nearest_intersection_other_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('location_of_grade_crossing_nearest_intersection_other_s_of_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('preemption_of_traffic_signals_observe_encroachment_near_crossing_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('preemption_of_traffic_signals_observe_encroachment_near_crossing_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('preemption_of_traffic_signals_observe_queuing_condition')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('preemption_of_traffic_signals_observe_simultaneous_interconnection_advance_of_crossing')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('preemption_of_traffic_signals_observe_supplemental_signage')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('preemption_of_traffic_signals_observe_traffic_clearance_time_adequate')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('preemption_of_traffic_signals_rail_preemption_warning_time_actual')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('preemption_of_traffic_signals_road_or_rail_Crossing_preemption_type')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('preemption_of_traffic_signals_road_preemption_warning_time_design')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('preemption_of_traffic_signals_warrant_proximity_condition')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('road_geometry_lookup_gradient_difference')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('road_geometry_measture_railway_cross_slope')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('road_geometry_measture_slope_between_8m_and_18m_nearest_rail_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('road_geometry_measture_slope_between_8m_and_18m_nearest_rail_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('road_geometry_measture_slope_Within_5m_nearest_rail_at_sidewalk')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('road_geometry_measture_slope_Within_8m_nearest_rail_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('road_geometry_measture_slope_Within_8m_nearest_rail_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('road_geometry_observe_alignment_horizontal_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('road_geometry_observe_alignment_horizontal_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('road_geometry_rail_superelevation')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('road_geometry_rail_superelevation_rate')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('road_geometry_road_crossing_angle')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('road_geometry_road_general_approach_grade_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('road_geometry_road_general_approach_grade_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_calculate_dssd_vehicle_min_ft')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_calculate_dssd_vehicle_min_m')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_calculate_dstopped_pedestrian_min_ft')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_calculate_dstopped_pedestrian_min_m')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_calculate_dstopped_vehicle_min_ft')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_calculate_dstopped_vehicle_min_m')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_lookup_stopping_sight_distance_minimum_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_lookup_stopping_sight_distance_minimum_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_measture_Dssd_actual_n_or_e_approach_driver_left')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_measture_Dssd_actual_n_or_e_approach_driver_right')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_measture_Dssd_actual_s_or_w_approach_driver_left')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_measture_Dssd_actual_s_or_w_approach_driver_right')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_measture_dstopped_actual_n_or_e_approach_driver_left')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_measture_dstopped_actual_n_or_e_approach_driver_right')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_measture_dstopped_actual_s_or_w_approach_driver_left')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_measture_dstopped_actual_s_or_w_approach_driver_right')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_measture_stopping_sight_distance_actual_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_measture_stopping_sight_distance_actual_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_observe_sightline_obstructions')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_buildings_ne')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_buildings_nw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_buildings_se')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_buildings_sw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_equipment_ne')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_equipment_nw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_equipment_se')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_equipment_sw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_horizontal_and_Vertical_alignment_rail_ne')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_horizontal_and_Vertical_alignment_rail_nw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_horizontal_and_Vertical_alignment_rail_se')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_horizontal_and_Vertical_alignment_rail_sw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_horizontal_and_Vertical_alignment_road_ne')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_horizontal_and_Vertical_alignment_road_nw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_horizontal_and_Vertical_alignment_road_se')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_horizontal_and_Vertical_alignment_road_sw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_other_ne')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_other_nw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_other_se')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_other_sw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_roadside_commercial_signing_ne')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_roadside_commercial_signing_nw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_roadside_commercial_signing_se')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_roadside_commercial_signing_sw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_topography_ne')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_topography_nw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_topography_se')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_topography_sw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_traffic_control_devices_ne')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_traffic_control_devices_nw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_traffic_control_devices_se')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_traffic_control_devices_sw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_Utility_and_lighting_poles_ne')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_Utility_and_lighting_poles_nw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_Utility_and_lighting_poles_se')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_Utility_and_lighting_poles_sw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_Vegetation_control_rail_row_ne')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_Vegetation_control_rail_row_nw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_Vegetation_control_rail_row_se')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_Vegetation_control_rail_row_sw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_Vegetation_control_road_row_ne')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_Vegetation_control_road_row_nw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_Vegetation_control_road_row_se')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_restrictions_Vegetation_control_road_row_sw')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_road_stopping_sight_distance_n_or_e_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('sightlines_road_stopping_sight_distance_s_or_w_approach')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_advisory_speed_n_or_e_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_advisory_speed_n_or_e_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_advisory_speed_n_or_e_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_advisory_speed_n_or_e_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_advisory_speed_s_or_w_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_advisory_speed_s_or_w_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_advisory_speed_s_or_w_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_advisory_speed_s_or_w_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_do_not_stop_on_track_n_or_e_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_do_not_stop_on_track_n_or_e_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_do_not_stop_on_track_n_or_e_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_do_not_stop_on_track_n_or_e_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_do_not_stop_on_track_s_or_w_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_do_not_stop_on_track_s_or_w_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_do_not_stop_on_track_s_or_w_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_do_not_stop_on_track_s_or_w_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_emergency_notification_n_or_e_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_emergency_notification_n_or_e_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_emergency_notification_n_or_e_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_emergency_notification_n_or_e_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_emergency_notification_s_or_w_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_emergency_notification_s_or_w_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_emergency_notification_s_or_w_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_emergency_notification_s_or_w_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_number_of_tracks_n_or_e_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_number_of_tracks_n_or_e_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_number_of_tracks_n_or_e_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_number_of_tracks_n_or_e_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_number_of_tracks_s_or_w_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_number_of_tracks_s_or_w_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_number_of_tracks_s_or_w_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_number_of_tracks_s_or_w_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_posted_speed_n_or_e_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_posted_speed_n_or_e_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_posted_speed_n_or_e_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_posted_speed_n_or_e_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_posted_speed_s_or_w_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_posted_speed_s_or_w_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_posted_speed_s_or_w_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_posted_speed_s_or_w_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_private_n_or_e_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_private_s_or_w_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_ahead_n_or_e_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_ahead_n_or_e_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_ahead_n_or_e_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_ahead_n_or_e_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_ahead_s_or_w_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_ahead_s_or_w_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_ahead_s_or_w_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_ahead_s_or_w_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_n_or_e_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_n_or_e_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_n_or_e_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_n_or_e_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_n_or_e_reflective_stripes_on_sign')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_n_or_e_approach_reflective_stripes_post_back')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_n_or_e_approach_reflective_stripes_post_front')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_s_or_w_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_s_or_w_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_s_or_w_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_s_or_w_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_s_or_w_approach_reflective_stripes_of_sign')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_s_or_w_approach_reflective_stripes_post_back')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_railway_crossing_s_or_w_approach_reflective_stripes_post_front')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_RR_crossing_symbols_n_or_e_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_RR_crossing_symbols_n_or_e_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_RR_crossing_symbols_n_or_e_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_RR_crossing_symbols_n_or_e_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_RR_crossing_symbols_s_or_w_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_RR_crossing_symbols_s_or_w_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_RR_crossing_symbols_s_or_w_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_RR_crossing_symbols_s_or_w_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_sidewalks_n_or_e_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_sidewalks_s_or_w_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stop_n_or_e_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stop_n_or_e_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stop_n_or_e_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stop_n_or_e_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stop_s_or_w_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stop_s_or_w_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stop_s_or_w_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stop_s_or_w_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stop_sign_Ahead_n_or_e_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stop_sign_Ahead_n_or_e_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stop_sign_Ahead_n_or_e_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stop_sign_Ahead_n_or_e_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stop_sign_Ahead_s_or_w_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stop_sign_Ahead_s_or_w_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stop_sign_Ahead_s_or_w_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stop_sign_Ahead_s_or_w_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stoplines_n_or_e_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stoplines_n_or_e_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stoplines_n_or_e_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stoplines_n_or_e_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stoplines_s_or_w_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stoplines_s_or_w_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stoplines_s_or_w_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_stoplines_s_or_w_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_train_whistle_Prohibited_n_or_e_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_train_whistle_Prohibited_n_or_e_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_train_whistle_Prohibited_n_or_e_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_train_whistle_Prohibited_n_or_e_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_train_whistle_Prohibited_s_or_w_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_train_whistle_Prohibited_s_or_w_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_train_whistle_Prohibited_s_or_w_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_train_whistle_Prohibited_s_or_w_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_Two_train_event_n_or_e_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_Two_train_event_n_or_e_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_Two_train_event_n_or_e_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_Two_train_event_n_or_e_approach_present')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_Two_train_event_s_or_w_approach_height')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_Two_train_event_s_or_w_approach_location_from_rail')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_Two_train_event_s_or_w_approach_location_from_road')
        )
        self.mapper.addMapping(
            self.view.temp,
            self.db.db_model_crossing_assessment_ca.fieldIndex('signs_and_pavement_markings_Two_train_event_s_or_w_approach_present')
        )  