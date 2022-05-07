from PyQt5 import QtWidgets as qtw

from .models.model_form_crossing_ca import ModelFormCrossingCA
from .views.view_form_crossing_ca import ViewFormCrossingCA

class FormGradeCrossingCA(qtw.QWidget):
    def __init__(self):
        super().__init__() # create default constructor for QWidget
        self.view = ViewFormCrossingCA()
        self.model = ModelFormCrossingCA(self.view)
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
        self.view.spinBox_collision_history_fatal_injury.valueChanged.connect(self.model.handle_collision_history_total_5_year_period)
        self.view.spinBox_collision_history_personal_injury.valueChanged.connect(self.model.handle_collision_history_total_5_year_period)
        self.view.spinBox_collision_history_property_damage.valueChanged.connect(self.model.handle_collision_history_total_5_year_period)
        
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
        self.view.spinBox_general_info_road_aadt_current.valueChanged.connect(self.model.handle_collision_history_risk_index_initial)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.handle_collision_history_risk_index_initial)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.handle_collision_history_risk_index_initial)
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.handle_collision_history_risk_index_initial)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.handle_collision_history_risk_index_initial)
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.handle_collision_history_risk_index_initial)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.handle_collision_history_risk_index_initial)
        self.view.spinBox_general_info_road_no_traffic_lanes_bidirectional.valueChanged.connect(self.model.handle_collision_history_risk_index_initial)
        self.view.spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound.valueChanged.connect(self.model.handle_collision_history_risk_index_initial)
        self.view.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound.valueChanged.connect(self.model.handle_collision_history_risk_index_initial)
        self.view.comboBox_inspection_details_gcws_type.currentTextChanged.connect(self.model.handle_collision_history_risk_index_initial)
        self.view.comboBox_general_info_road_classification.currentTextChanged.connect(self.model.handle_collision_history_risk_index_initial)
        self.view.comboBox_grade_crossing_surface_observe_road_approach_surface_type.currentTextChanged.connect(self.model.handle_collision_history_risk_index_initial)
        self.view.comboBox_gcws_observe_gates_n_or_e_approach.currentTextChanged.connect(self.model.handle_collision_history_risk_index_initial)
        self.view.comboBox_gcws_observe_gates_s_or_w_approach.currentTextChanged.connect(self.model.handle_collision_history_risk_index_initial)
        
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

        self.view.spinBox_general_info_road_aadt_current.valueChanged.connect(self.model.handle_collision_history_risk_index_final)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.handle_collision_history_risk_index_final)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.handle_collision_history_risk_index_final)
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.handle_collision_history_risk_index_final)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.handle_collision_history_risk_index_final)
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.handle_collision_history_risk_index_final)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.handle_collision_history_risk_index_final)
        self.view.spinBox_general_info_road_no_traffic_lanes_bidirectional.valueChanged.connect(self.model.handle_collision_history_risk_index_final)
        self.view.spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound.valueChanged.connect(self.model.handle_collision_history_risk_index_final)
        self.view.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound.valueChanged.connect(self.model.handle_collision_history_risk_index_final)
        self.view.comboBox_inspection_details_gcws_type.currentTextChanged.connect(self.model.handle_collision_history_risk_index_final)
        self.view.comboBox_general_info_road_classification.currentTextChanged.connect(self.model.handle_collision_history_risk_index_final)
        self.view.comboBox_grade_crossing_surface_observe_road_approach_surface_type.currentTextChanged.connect(self.model.handle_collision_history_risk_index_final)
        self.view.comboBox_gcws_observe_gates_n_or_e_approach.currentTextChanged.connect(self.model.handle_collision_history_risk_index_final)
        self.view.comboBox_gcws_observe_gates_s_or_w_approach.currentTextChanged.connect(self.model.handle_collision_history_risk_index_final)
        self.view.spinBox_collision_history_fatal_injury.valueChanged.connect(self.model.handle_collision_history_risk_index_final)
        self.view.spinBox_collision_history_personal_injury.valueChanged.connect(self.model.handle_collision_history_risk_index_final)
        self.view.spinBox_collision_history_property_damage.valueChanged.connect(self.model.handle_collision_history_risk_index_final)

        # GENERAL INFORMATION
        #general_info_rail_no_tracks_total - connect signals and slots
        '''
        Connect input variable signals to general_info_rail_no_tracks_total method slot.
        Required input variables: 
            spinBox_general_info_rail_no_tracks_main, spinBox_general_info_rail_no_tracks_other
        Related methods:
            None
        '''
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.handle_general_info_rail_no_tracks_total)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.handle_general_info_rail_no_tracks_total)
        
        #general_info_rail_no_trains_per_day_total - connect signals and slots
        '''
        Connect input variable signals to general_info_rail_no_trains_per_day_total method slot.
        Required input variables: 
            spinBox_general_info_rail_no_trains_per_day_freight, spinBox_general_info_rail_no_trains_per_day_passengers
        Related methods:
            None
        '''
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.handle_general_info_rail_no_trains_per_day_total)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.handle_general_info_rail_no_trains_per_day_total)
        
        #general_info_road_no_traffic_lanes_total - connect signals and slots
        '''
        Connect input variable signals to general_info_road_no_traffic_lanes_total method slot.
        Required input variables: 
            spinBox_general_info_road_no_traffic_lanes_bidirectional, spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound, spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound
        Related methods:
            None
        '''
        self.view.spinBox_general_info_road_no_traffic_lanes_bidirectional.valueChanged.connect(self.model.handle_general_info_road_no_traffic_lanes_total)
        self.view.spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound.valueChanged.connect(self.model.handle_general_info_road_no_traffic_lanes_total)
        self.view.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound.valueChanged.connect(self.model.handle_general_info_road_no_traffic_lanes_total)
        
        #general_info_rail_railway_design_speed - connect signals and slots
        '''
        Connect input variable signals to general_info_rail_railway_design_speed method slot.
        Required input variables: 
            spinBox_general_info_rail_max_railway_operating_speed_freight, spinBox_general_info_rail_max_railway_operating_speed_passenger
        Related methods:
            None
        '''
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.handle_general_info_rail_railway_design_speed)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.handle_general_info_rail_railway_design_speed)        
        
        # DESIGN CONSIDERATIONS (GCS SECTION 10)
        #design_calculate_adjacent_track_clearance_time - connect signals and slots
        '''
        Connect input variable signals to design_calculate_adjacent_track_clearance_time method slot.
        Required input variables: 
            doubleSpinBox_design_measure_adjacent_track_separation_distance, doubleSpinBox_design_measure_adjacent_track_clearance_distance
        Related methods:
            None
        '''
        self.view.doubleSpinBox_design_measure_adjacent_track_separation_distance.valueChanged.connect(self.model.handle_design_calculate_adjacent_track_clearance_time)
        self.view.doubleSpinBox_design_measure_adjacent_track_clearance_distance.valueChanged.connect(self.model.handle_design_calculate_adjacent_track_clearance_time)

        #design_calculate_clearance_time_crossing_pedestrian_design_check - connect signals and slots
        '''
        Connect input variable signals to design_calculate_clearance_time_crossing_pedestrian_design_check method slot.
        Required input variables: 
            doubleSpinBox_design_measure_clearance_distance_pedestrian
        Related methods:
            None
        '''
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.handle_design_calculate_clearance_time_pedestrian_design_check)

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
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.handle_design_calculate_clearance_time_vehicle_design_check)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.handle_design_calculate_clearance_time_vehicle_design_check)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.handle_design_calculate_clearance_time_vehicle_design_check)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_design_calculate_clearance_time_vehicle_design_check)                                                                     

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
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.handle_design_calculate_gate_arm_clearance_time_vehicle_ssd)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.handle_design_calculate_gate_arm_clearance_time_vehicle_ssd)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.handle_design_calculate_gate_arm_clearance_time_vehicle_ssd)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_design_calculate_gate_arm_clearance_time_vehicle_ssd)

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
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.handle_design_calculate_gate_arm_clearance_time_vehicle_stop)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.handle_design_calculate_gate_arm_clearance_time_vehicle_stop)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_design_calculate_gate_arm_clearance_time_vehicle_stop)

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
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.handle_design_calculate_gate_arm_clearance_time_vehicle_recommended)
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.handle_design_calculate_gate_arm_clearance_time_vehicle_recommended)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.handle_design_calculate_gate_arm_clearance_time_vehicle_recommended)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.handle_design_calculate_gate_arm_clearance_time_vehicle_recommended)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.handle_design_calculate_gate_arm_clearance_time_vehicle_recommended)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_design_calculate_gate_arm_clearance_time_vehicle_recommended)

        #design_calculate_vehicle_travel_distance - connect signals and slots
        '''
        Connect input variable signals to design_calculate_vehicle_travel_distance method slot.
        Required input variables:
            doubleSpinBox_design_measure_clearance_distance_vehicle
            comboBox_design_road_design_vehicle_type
        Related methods:
            handle_design_lookup_design_vehicle_length 
        ''' 
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.handle_design_calculate_vehicle_travel_distance)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_design_calculate_vehicle_travel_distance)
        
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
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.handle_design_calculate_vehicle_departure_time)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.handle_design_calculate_vehicle_departure_time)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_design_calculate_vehicle_departure_time)

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
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.handle_design_calculate_vehicle_departure_time_grade_adjusted)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.handle_design_calculate_vehicle_departure_time_grade_adjusted)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(lambda val:self.model.handle_design_calculate_vehicle_departure_time_grade_adjusted)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_design_calculate_vehicle_departure_time_grade_adjusted)

        #design_calculate_vehicle_departure_time_gate_arm_clearance - connect signals and slots
        '''
        Connect input variable signals to design_calculate_vehicle_departure_time_gate_arm_clearance method slot.
        Required input variables:
            comboBox_design_road_design_vehicle_type
        Related methods:    
            handle_design_lookup_design_vehicle_class
            handle_design_lookup_design_vehicle_length
        '''
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_design_calculate_vehicle_departure_time_gate_arm_clearance)
        
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
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.handle_design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted)

        #design_lookup_design_vehicle_class - connect signals and slots
        '''
        Connect input variable signals to design_lookup_design_vehicle_class method slot.
        Required input variables: 
            comboBox_design_road_design_vehicle_type
        Related methods:
            None
        ''' 
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_design_lookup_design_vehicle_class)

        #design_lookup_design_vehicle_length - connect signals and slots
        '''
        Connect input variable signals to design_lookup_design_vehicle_length method slot.
        Required input variables: 
            comboBox_design_road_design_vehicle_type
        Related methods:
            None
        ''' 
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_design_lookup_design_vehicle_length)
                
        #design_lookup_grade_adjustment_factor - connect signals and slots
        '''
        Connect input variable signals to design_lookup_grade_adjustment_factor method slot.
        Required input variables:
            doubleSpinBox_design_road_max_approach_grade_within_s
            comboBox_design_road_design_vehicle_type
        Related methods:
            None
        ''' 
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.handle_design_lookup_grade_adjustment_factor)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_design_lookup_grade_adjustment_factor)

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
        self.view.comboBox_general_info_road_classification.currentTextChanged.connect(self.model.handle_road_geometry_lookup_gradient_difference)
        
        # SIGHTLINES (GCS SECTION 7)
        #sightlines_lookup_existing_active_crossing - connect signals and slots
        '''
        Connect input variable signals to sightlines_lookup_existing_active_crossing method slot.
        Required input variables:
            comboBox_inspection_details_gcws_type
        Related methods:
            None
        ''' 
        self.view.comboBox_inspection_details_gcws_type.currentTextChanged.connect(self.model.handle_sightlines_lookup_existing_active_crossing)
        
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
        self.view.comboBox_inspection_details_gcws_type.currentTextChanged.connect(self.model.handle_sightlines_lookup_existing_active_crossing_with_gates)
        self.view.comboBox_gcws_observe_gates_n_or_e_approach.currentTextChanged.connect(self.model.handle_sightlines_lookup_existing_active_crossing_with_gates)
        self.view.comboBox_gcws_observe_gates_s_or_w_approach.currentTextChanged.connect(self.model.handle_sightlines_lookup_existing_active_crossing_with_gates)

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
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.handle_sightlines_calculate_dstopped_pedestrian_min_ft)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.handle_sightlines_calculate_dstopped_pedestrian_min_ft)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.handle_sightlines_calculate_dstopped_pedestrian_min_ft)

        #sightlines_calculate_dstopped_pedestrian_min_m - connect signals and slots
        '''
        Connect input variable signals to sightlines_calculate_dstopped_pedestrian_min_m method slot.
        Required input variables:
            doubleSpinBox_design_measure_clearance_distance_pedestrian
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
        Related methods: 
            self.model.handle_design_calculate_clearance_time_pedestrian_design_check       
            handle_general_info_rail_railway_design_speed
        '''
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.handle_sightlines_calculate_dstopped_pedestrian_min_m)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.handle_sightlines_calculate_dstopped_pedestrian_min_m)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.handle_sightlines_calculate_dstopped_pedestrian_min_m)

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
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.handle_sightlines_calculate_dstopped_vehicle_min_ft)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.handle_sightlines_calculate_dstopped_vehicle_min_ft)
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.handle_sightlines_calculate_dstopped_vehicle_min_ft)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.handle_sightlines_calculate_dstopped_vehicle_min_ft)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.handle_sightlines_calculate_dstopped_vehicle_min_ft)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_sightlines_calculate_dstopped_vehicle_min_ft)

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
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.handle_sightlines_calculate_dstopped_vehicle_min_m)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.handle_sightlines_calculate_dstopped_vehicle_min_m)
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.handle_sightlines_calculate_dstopped_vehicle_min_m)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.handle_sightlines_calculate_dstopped_vehicle_min_m)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.handle_sightlines_calculate_dstopped_vehicle_min_m)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_sightlines_calculate_dstopped_vehicle_min_m)

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
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.handle_sightlines_lookup_ssd_minimum_n_or_e_approach)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.handle_sightlines_lookup_ssd_minimum_n_or_e_approach)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_sightlines_lookup_ssd_minimum_n_or_e_approach)

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
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.handle_sightlines_lookup_ssd_minimum_s_or_w_approach)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.handle_sightlines_lookup_ssd_minimum_s_or_w_approach)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_sightlines_lookup_ssd_minimum_s_or_w_approach)

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
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.handle_sightlines_calculate_dssd_vehicle_min_ft)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.handle_sightlines_calculate_dssd_vehicle_min_ft)
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.handle_sightlines_calculate_dssd_vehicle_min_ft)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.handle_sightlines_calculate_dssd_vehicle_min_ft)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.handle_sightlines_calculate_dssd_vehicle_min_ft)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.handle_sightlines_calculate_dssd_vehicle_min_ft)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_sightlines_calculate_dssd_vehicle_min_ft)
        
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
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.handle_sightlines_calculate_dssd_vehicle_min_m)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.handle_sightlines_calculate_dssd_vehicle_min_m)
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.handle_sightlines_calculate_dssd_vehicle_min_m)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.handle_sightlines_calculate_dssd_vehicle_min_m)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.handle_sightlines_calculate_dssd_vehicle_min_m)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.handle_sightlines_calculate_dssd_vehicle_min_m)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_sightlines_calculate_dssd_vehicle_min_m)

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
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_gcws_rail_design_warning_time_clearance_distance)
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.handle_gcws_rail_design_warning_time_clearance_distance)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.handle_gcws_rail_design_warning_time_clearance_distance)
        
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
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.handle_gcws_rail_design_warning_time_departure_time_vehicle)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.handle_gcws_rail_design_warning_time_departure_time_vehicle)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.handle_gcws_rail_design_warning_time_departure_time_vehicle)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_gcws_rail_design_warning_time_departure_time_vehicle)

        #gcws_rail_design_warning_time_departure_time_pedestrian - connect signals and slots
        '''
        Connect input variable signals to gcws_rail_design_warning_time_departure_time_pedestrian method slot.
        Required input variables:
            doubleSpinBox_design_measure_clearance_distance_pedestrian
        Related methods:
            self.model.handle_design_calculate_clearance_time_pedestrian_design_check
        '''
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.handle_gcws_rail_design_warning_time_departure_time_pedestrian)

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
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.handle_gcws_rail_design_warning_time_gate_arm_clearance)
        #TODO Remove Pedestrian clearance distance
        # self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.handle_gcws_rail_design_warning_time_gate_arm_clearance('doubleSpinBox_design_measure_clearance_distance_pedestrian', val))
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.handle_gcws_rail_design_warning_time_gate_arm_clearance)
        self.view.doubleSpinBox_gates_gcws_rail_gate_arm_descent_time_design.valueChanged.connect(self.model.handle_gcws_rail_design_warning_time_gate_arm_clearance)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.handle_gcws_rail_design_warning_time_gate_arm_clearance)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.handle_gcws_rail_design_warning_time_gate_arm_clearance)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_gcws_rail_design_warning_time_gate_arm_clearance)
        
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
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.handle_gcws_rail_design_warning_time_ssd)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.handle_gcws_rail_design_warning_time_ssd)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.handle_gcws_rail_design_warning_time_ssd)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.handle_gcws_rail_design_warning_time_ssd)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_gcws_rail_design_warning_time_ssd)

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
        self.view.doubleSpinBox_design_measure_adjacent_track_separation_distance.valueChanged.connect(self.model.handle_gates_gcws_calculate_inner_gate_arm_delay_time_recommended)
        self.view.doubleSpinBox_design_measure_adjacent_track_clearance_distance.valueChanged.connect(self.model.handle_gates_gcws_calculate_inner_gate_arm_delay_time_recommended)

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
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.handle_aawd_calculate_advance_activation_time_design_n_or_e_approach)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.handle_aawd_calculate_advance_activation_time_design_n_or_e_approach)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.handle_aawd_calculate_advance_activation_time_design_n_or_e_approach)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.handle_aawd_calculate_advance_activation_time_design_n_or_e_approach)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_aawd_calculate_advance_activation_time_design_n_or_e_approach)
        
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
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.handle_aawd_calculate_advance_activation_time_design_s_or_w_approach)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.handle_aawd_calculate_advance_activation_time_design_s_or_w_approach)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.handle_aawd_calculate_advance_activation_time_design_s_or_w_approach)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.handle_aawd_calculate_advance_activation_time_design_s_or_w_approach)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.handle_aawd_calculate_advance_activation_time_design_s_or_w_approach)

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
        self.view.spinBox_general_info_road_speed_posted.valueChanged.connect(self.model.handle_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.handle_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended)  
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.handle_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended)  

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
        self.view.spinBox_general_info_road_speed_posted.valueChanged.connect(self.model.handle_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.handle_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended)  
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.handle_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended)

        #TODO
        #aawd_warrant_gcr_lookup_road_classification - connect signals and slots
        '''
        Connect input variable signals to aawd_warrant_gcr_lookup_road_classification method slot.
        Required input variables:
            comboBox_general_info_road_classification
        Related methods:
            None
        '''
        self.view.comboBox_general_info_road_classification.currentTextChanged.connect(self.model.handle_aawd_warrant_gcr_lookup_road_classification)

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