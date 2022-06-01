import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtSql as qts

from gradecrossingform.models.model_form_crossing_ca import ModelCrossingAssessmentCA
from gradecrossingform.views.view_form_xing_assessment_ca import ViewCrossingAssessmentCA

class ControllerCrossingAssessmentCA(qtw.QWidget):
    def __init__(self):
        super().__init__() # create default constructor for QWidget
        self.view = ViewCrossingAssessmentCA()
        self.model = ModelCrossingAssessmentCA(self.view)
        self.connect_and_emit_trigger()

        '''DATABASE SAMPLE CODE START

        # Connect to the database
        self.db = qts.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('app\custom\GradeCrossingForm\db\sqllite\db_sqllite_grade_crossing.db')
        if not self.db.open():
            error = self.db.lastError().text()
            qtw.QMessageBox.critical(
                None, 'DB Connection Error',
                'Could not open database file: '
                f'{error}')
            sys.exit(1)

        # Check for missing tables
        required_tables = {'roasts', 'crossing_ca_inventory', 'reviews'}
        tables = self.db.tables()
        missing_tables = required_tables - set(tables)
        if missing_tables:
            qtw.QMessageBox.critical(
                None, 'DB Integrity Error',
                'Missing tables, please repair DB: '
                f'{missing_tables}')
            sys.exit(1)

        # Make a query
        query = self.db.exec('SELECT count(*) FROM crossing_ca_inventory')
        query.next()
        count = query.value(0)
        print(f'There are {count} crossing_ca_inventory in the database.')

        # Retreive the roasts table
        query = self.db.exec('SELECT * FROM roasts ORDER BY id')
        roasts = []
        while query.next():
            roasts.append(query.value(1))

        # create the form
        self.coffee_form = CoffeeForm(roasts)
        self.stack.addWidget(self.coffee_form)

        # Retreive the crossing_ca_inventory table using a QSqlQueryModel
        crossing_ca_inventory = qts.QSqlQueryModel()
        crossing_ca_inventory.setQuery(
            "SELECT id, coffee_brand, coffee_name AS coffee "
            "FROM crossing_ca_inventory ORDER BY id")
        self.coffee_list = qtw.QTableView()
        self.coffee_list.setModel(crossing_ca_inventory)
        self.stack.addWidget(self.coffee_list)
        self.stack.setCurrentWidget(self.coffee_list)

        crossing_ca_inventory.setHeaderData(1, qtc.Qt.Horizontal, 'Brand')
        crossing_ca_inventory.setHeaderData(2, qtc.Qt.Horizontal, 'Product')

        # Navigation between stacked widgets
        navigation = self.addToolBar("Navigation")
        navigation.addAction(
            "Back to list",
            lambda: self.stack.setCurrentWidget(self.coffee_list))

        self.coffee_list.doubleClicked.connect(
            lambda x: self.show_coffee(self.get_id_for_row(x)))

        # Code ends here
        self.show()

        DATABASE SAMPLE CODE END'''

    def connect_and_emit_trigger(self):
        #connecting a signal to python callables
        # COLLISION HISTORY (5 YEAR PERIOD)
        #connect signals and slots - collision_history_total_5_year_period
        '''
        Connect input variable signals to collision_history_total_5_year_period method slot.
        Required input variables: 
            spinBox_collision_history_fatal_injury, spinBox_collision_history_personal_injury, spinBox_collision_history_property_damage
        Related methods:
            None
        '''
        self.view.spinBox_collision_history_fatal_injury.valueChanged.connect(self.model.collision_history_total_5_year_period)
        self.view.spinBox_collision_history_personal_injury.valueChanged.connect(self.model.collision_history_total_5_year_period)
        self.view.spinBox_collision_history_property_damage.valueChanged.connect(self.model.collision_history_total_5_year_period)
        
        #connect signals and slots - collision_history_risk_index_initial
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
        self.view.spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound.valueChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound.valueChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.comboBox_inspection_details_gcws_type.currentTextChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.comboBox_general_info_road_classification.currentTextChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.comboBox_grade_crossing_surface_observe_road_approach_surface_type.currentTextChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.comboBox_gcws_observe_gates_n_or_e_approach.currentTextChanged.connect(self.model.collision_history_risk_index_initial)
        self.view.comboBox_gcws_observe_gates_s_or_w_approach.currentTextChanged.connect(self.model.collision_history_risk_index_initial)
        
        #connect signals and slots - collision_history_risk_index_final
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
        self.view.spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound.valueChanged.connect(self.model.collision_history_risk_index_final)
        self.view.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound.valueChanged.connect(self.model.collision_history_risk_index_final)
        self.view.comboBox_inspection_details_gcws_type.currentTextChanged.connect(self.model.collision_history_risk_index_final)
        self.view.comboBox_general_info_road_classification.currentTextChanged.connect(self.model.collision_history_risk_index_final)
        self.view.comboBox_grade_crossing_surface_observe_road_approach_surface_type.currentTextChanged.connect(self.model.collision_history_risk_index_final)
        self.view.comboBox_gcws_observe_gates_n_or_e_approach.currentTextChanged.connect(self.model.collision_history_risk_index_final)
        self.view.comboBox_gcws_observe_gates_s_or_w_approach.currentTextChanged.connect(self.model.collision_history_risk_index_final)
        self.view.spinBox_collision_history_fatal_injury.valueChanged.connect(self.model.collision_history_risk_index_final)
        self.view.spinBox_collision_history_personal_injury.valueChanged.connect(self.model.collision_history_risk_index_final)
        self.view.spinBox_collision_history_property_damage.valueChanged.connect(self.model.collision_history_risk_index_final)

        # GENERAL INFORMATION
        #connect signals and slots - general_info_rail_no_tracks_total
        '''
        Connect input variable signals to general_info_rail_no_tracks_total method slot.
        Required input variables: 
            spinBox_general_info_rail_no_tracks_main, spinBox_general_info_rail_no_tracks_other
        Related methods:
            None
        '''
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.general_info_rail_no_tracks_total)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.general_info_rail_no_tracks_total)
        
        #connect signals and slots - general_info_rail_no_trains_per_day_total
        '''
        Connect input variable signals to general_info_rail_no_trains_per_day_total method slot.
        Required input variables: 
            spinBox_general_info_rail_no_trains_per_day_freight, spinBox_general_info_rail_no_trains_per_day_passengers
        Related methods:
            None
        '''
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.general_info_rail_no_trains_per_day_total)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.general_info_rail_no_trains_per_day_total)
        
        #connect signals and slots - general_info_road_no_traffic_lanes_total
        '''
        Connect input variable signals to general_info_road_no_traffic_lanes_total method slot.
        Required input variables: 
            spinBox_general_info_road_no_traffic_lanes_bidirectional, spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound, spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound
        Related methods:
            None
        '''
        self.view.spinBox_general_info_road_no_traffic_lanes_bidirectional.valueChanged.connect(self.model.general_info_road_no_traffic_lanes_total)
        self.view.spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound.valueChanged.connect(self.model.general_info_road_no_traffic_lanes_total)
        self.view.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound.valueChanged.connect(self.model.general_info_road_no_traffic_lanes_total)
        
        #connect signals and slots - general_info_rail_railway_design_speed
        '''
        Connect input variable signals to general_info_rail_railway_design_speed method slot.
        Required input variables: 
            spinBox_general_info_rail_max_railway_operating_speed_freight, spinBox_general_info_rail_max_railway_operating_speed_passenger
        Related methods:
            None
        '''
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.general_info_rail_railway_design_speed)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.general_info_rail_railway_design_speed)        
        
        # DESIGN CONSIDERATIONS (GCS SECTION 10)
        #connect signals and slots - design_calculate_adjacent_track_clearance_time
        '''
        Connect input variable signals to design_calculate_adjacent_track_clearance_time method slot.
        Required input variables: 
            doubleSpinBox_design_measure_adjacent_track_separation_distance, doubleSpinBox_design_measure_adjacent_track_clearance_distance
        Related methods:
            None
        '''
        self.view.doubleSpinBox_design_measure_adjacent_track_separation_distance.valueChanged.connect(self.model.design_calculate_adjacent_track_clearance_time)
        self.view.doubleSpinBox_design_measure_adjacent_track_clearance_distance.valueChanged.connect(self.model.design_calculate_adjacent_track_clearance_time)

        #connect signals and slots - design_calculate_clearance_time_crossing_pedestrian_design_check
        '''
        Connect input variable signals to design_calculate_clearance_time_crossing_pedestrian_design_check method slot.
        Required input variables: 
            doubleSpinBox_design_measure_clearance_distance_pedestrian
        Related methods:
            None
        '''
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.design_calculate_clearance_time_pedestrian_design_check)

        #connect signals and slots - design_calculate_clearance_time_vehicle_design_check
        '''
        Connect input variable signals to design_calculate_clearance_time_vehicle_design_check method slot.
        Required input variables: 
            doubleSpinBox_design_measure_clearance_distance_pedestrian
            doubleSpinBox_design_measure_clearance_distance_vehicle
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
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.design_calculate_clearance_time_vehicle_design_check)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.design_calculate_clearance_time_vehicle_design_check)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.design_calculate_clearance_time_vehicle_design_check)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_calculate_clearance_time_vehicle_design_check)                                                                     

        #TODO 
        #self.label_design_measure_clearance_distance_gate_arm_ssd = qtw.QLabel('No Value')

        #connect signals and slots - design_calculate_gate_arm_clearance_time_vehicle_ssd
        '''
        Connect input variable signals to design_calculate_gate_arm_clearance_time_vehicle_ssd method slot.
        Required input variables: 
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
        Required input variables:
            doubleSpinBox_design_measure_clearance_distance_pedestrian 
            doubleSpinBox_design_road_max_approach_grade_within_s
            comboBox_design_road_design_vehicle_type
        Related methods:
            label_design_input_reaction_time
            design_calculate_vehicle_departure_time_gate_arm_clearance
            design_lookup_grade_adjustment_factor
            design_lookup_design_vehicle_class
            design_lookup_design_vehicle_length
        '''
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_stop)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_stop)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_stop)

        #connect signals and slots - design_calculate_gate_arm_clearance_time_vehicle_recommended
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
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_recommended)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_recommended)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_recommended)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_recommended)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_calculate_gate_arm_clearance_time_vehicle_recommended)

        #connect signals and slots - design_calculate_vehicle_travel_distance
        '''
        Connect input variable signals to design_calculate_vehicle_travel_distance method slot.
        Required input variables:
            doubleSpinBox_design_measure_clearance_distance_vehicle
            comboBox_design_road_design_vehicle_type
        Related methods:
            design_lookup_design_vehicle_length 
        ''' 
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.design_calculate_vehicle_travel_distance)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_calculate_vehicle_travel_distance)
        
        #connect signals and slots - design_calculate_vehicle_departure_time
        '''
        Connect input variable signals to design_calculate_vehicle_departure_time method slot.
        Required input variables:
            doubleSpinBox_design_measure_clearance_distance_pedestrian
            doubleSpinBox_design_measure_clearance_distance_vehicle
            comboBox_design_road_design_vehicle_type
        Related methods:
            design_calculate_vehicle_travel_distance
            design_lookup_design_vehicle_class
            design_lookup_design_vehicle_length
        ''' 
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.design_calculate_vehicle_departure_time)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.design_calculate_vehicle_departure_time)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_calculate_vehicle_departure_time)

        #connect signals and slots - design_calculate_vehicle_departure_time_grade_adjusted
        '''
        Connect input variable signals to design_calculate_vehicle_departure_time_grade_adjusted method slot.
        Required input variables:
           doubleSpinBox_design_measure_clearance_distance_pedestrian
           doubleSpinBox_design_measure_clearance_distance_vehicle
           doubleSpinBox_design_road_max_approach_grade_within_s
           comboBox_design_road_design_vehicle_type
        Related methods:
            design_calculate_vehicle_departure_time
            design_calculate_vehicle_travel_distance
            design_lookup_design_vehicle_class
            design_lookup_design_vehicle_length
            design_lookup_grade_adjustment_factor
        '''
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.design_calculate_vehicle_departure_time_grade_adjusted)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.design_calculate_vehicle_departure_time_grade_adjusted)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(lambda val:self.model.design_calculate_vehicle_departure_time_grade_adjusted)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_calculate_vehicle_departure_time_grade_adjusted)

        #connect signals and slots - design_calculate_vehicle_departure_time_gate_arm_clearance
        '''
        Connect input variable signals to design_calculate_vehicle_departure_time_gate_arm_clearance method slot.
        Required input variables:
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
        Required input variables:
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
        Required input variables: 
            comboBox_design_road_design_vehicle_type
        Related methods:
            None
        ''' 
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_lookup_design_vehicle_class)

        #connect signals and slots - design_lookup_design_vehicle_length
        '''
        Connect input variable signals to design_lookup_design_vehicle_length method slot.
        Required input variables: 
            comboBox_design_road_design_vehicle_type
        Related methods:
            None
        ''' 
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_lookup_design_vehicle_length)
                
        #connect signals and slots - design_lookup_grade_adjustment_factor
        '''
        Connect input variable signals to design_lookup_grade_adjustment_factor method slot.
        Required input variables:
            doubleSpinBox_design_road_max_approach_grade_within_s
            comboBox_design_road_design_vehicle_type
        Related methods:
            None
        ''' 
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.design_lookup_grade_adjustment_factor)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.design_lookup_grade_adjustment_factor)

        #TODO
        #connect signals and slots - design_measure_clearance_distance_gate_arm_stop

        # ROAD GEOMETRY (GCS SECTION 6)
        #connect signals and slots - road_geometry_lookup_gradient_difference
        '''
        Connect input variable signals to road_geometry_lookup_gradient_difference method slot.
        Required input variables:
            comboBox_general_info_road_classification
        Related methods:
            None
        ''' 
        self.view.comboBox_general_info_road_classification.currentTextChanged.connect(self.model.road_geometry_lookup_gradient_difference)
        
        # SIGHTLINES (GCS SECTION 7)
        #connect signals and slots - sightlines_lookup_existing_active_crossing
        '''
        Connect input variable signals to sightlines_lookup_existing_active_crossing method slot.
        Required input variables:
            comboBox_inspection_details_gcws_type
        Related methods:
            None
        ''' 
        self.view.comboBox_inspection_details_gcws_type.currentTextChanged.connect(self.model.sightlines_lookup_existing_active_crossing)
        
        #connect signals and slots - sightlines_lookup_existing_active_crossing_with_gates
        '''
        Connect input variable signals to sightlines_lookup_existing_active_crossing_with_gates method slot.
        Required input variables:
            comboBox_inspection_details_gcws_type
            comboBox_gcws_observe_gates_n_or_e_approach
            comboBox_gcws_observe_gates_s_or_w_approach
        Related methods:
            None
        '''
        self.view.comboBox_inspection_details_gcws_type.currentTextChanged.connect(self.model.sightlines_lookup_existing_active_crossing_with_gates)
        self.view.comboBox_gcws_observe_gates_n_or_e_approach.currentTextChanged.connect(self.model.sightlines_lookup_existing_active_crossing_with_gates)
        self.view.comboBox_gcws_observe_gates_s_or_w_approach.currentTextChanged.connect(self.model.sightlines_lookup_existing_active_crossing_with_gates)

        # connect signals and slots - sightlines_calculate_dstopped_pedestrian_min_ft
        '''
        Connect input variable signals to sightlines_calculate_dstopped_pedestrian_min_ft method slot.
        Required input variables:
            doubleSpinBox_design_measure_clearance_distance_pedestrian
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
        Related methods: 
            design_calculate_clearance_time_pedestrian_design_check       
            general_info_rail_railway_design_speed
        '''
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.sightlines_calculate_dstopped_pedestrian_min_ft)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.sightlines_calculate_dstopped_pedestrian_min_ft)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.sightlines_calculate_dstopped_pedestrian_min_ft)

        #connect signals and slots - sightlines_calculate_dstopped_pedestrian_min_m
        '''
        Connect input variable signals to sightlines_calculate_dstopped_pedestrian_min_m method slot.
        Required input variables:
            doubleSpinBox_design_measure_clearance_distance_pedestrian
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
        Related methods: 
            self.model.design_calculate_clearance_time_pedestrian_design_check       
            general_info_rail_railway_design_speed
        '''
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.sightlines_calculate_dstopped_pedestrian_min_m)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.sightlines_calculate_dstopped_pedestrian_min_m)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.sightlines_calculate_dstopped_pedestrian_min_m)

        #TODO contains pedestrian clearance distance
        #connect signals and slots - sightlines_calculate_dstopped_vehicle_min_ft
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
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_ft)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_ft)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_ft)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_ft)

        #connect signals and slots - sightlines_calculate_dstopped_vehicle_min_m
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
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_m)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_m)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_m)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.sightlines_calculate_dstopped_vehicle_min_m)

        #connect signals and slots - sightlines_lookup_ssd_minimum_n_or_e_approach
        '''
        Connect input variable signals to sightlines_lookup_ssd_minimum_n_or_e_approach method slot.
        Required input variables:
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
        Required input variables:
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
        Required input variables:
            spinBox_general_info_rail_max_railway_operating_speed_freight
            spinBox_general_info_rail_max_railway_operating_speed_passenger
            spinBox_general_info_road_speed_design
            doubleSpinBox_design_measure_clearance_distance_vehicle
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
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_ft)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_ft)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_ft)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_ft)
        
        #connect signals and slots - sightlines_calculate_dssd_vehicle_min_m
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
            design_lookup_design_vehicle_class
            design_lookup_design_vehicle_length
            general_info_rail_railway_design_speed
            sightlines_lookup_ssd_minimum_n_or_e_approach
            sightlines_lookup_ssd_minimum_s_or_w_approach
        '''
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_m)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_m)
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_m)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_m)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_m)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_m)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.sightlines_calculate_dssd_vehicle_min_m)

        # GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
        #TODO
        #connect signals and slots - gcws_warrant_private_9_3
        # .valueChanged.connect(self.gcws_warrant_private_9_3)

        #connect signals and slots - gcws_warrant_private_9_3_1
        '''
        Connect input variable signals to gcws_warrant_private_9_3_1 method slot.
        Required input variables:
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
        Required input variables:
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
        Required input variables:
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
        Required input variables:
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
        Required input variables:
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
        Required input variables:
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
        Required input variables:
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
        Required input variables:
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
        Required input variables:
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
        Required input variables:
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
        #TODO add Design Vehcile Pedestrian
        '''
        Connect input variable signals to gcws_warrant_sidewalk_9_5 method slot.
        Required input variables:
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
        Required input variables:
            GCWS Private Warrants
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
            GCWS Private Warrants
            gcws_warrant_private_9_3_1
            gcws_warrant_private_9_3_2_a
            gcws_warrant_private_9_3_2_b
            gcws_warrant_private_9_3_2_c
            general_info_rail_no_tracks_total
            general_info_rail_no_trains_per_day_total
            general_info_rail_railway_design_speed    
        '''
        #GCWS Private Warrants
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
        Required input variables:
            GCWS Private Warrants
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
            GCWS Private Warrants
            gcws_warrant_private_9_3_1
            gcws_warrant_private_9_3_2_a
            gcws_warrant_private_9_3_2_b
            gcws_warrant_private_9_3_2_c
            general_info_rail_no_tracks_total
            general_info_rail_no_trains_per_day_total
            general_info_rail_railway_design_speed    
        '''
        #GCWS Private Warrants
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
        Required input variables:
            GCWS Private Warrants
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
            GCWS Private Warrants
            gcws_warrant_private_9_3_1
            gcws_warrant_private_9_3_2_a
            gcws_warrant_private_9_3_2_b
            gcws_warrant_private_9_3_2_c
            general_info_rail_no_tracks_total
            general_info_rail_no_trains_per_day_total
            general_info_rail_railway_design_speed    
        '''
        #GCWS Private Warrants
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
        Required input variables:
            GCWS Public Warrants
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
            GCWS Public Warrants
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
        Required input variables:
            GCWS Public Warrants
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
            GCWS Public Warrants
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
        Required input variables:
            GCWS Public Warrants
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
            GCWS Public Warrants
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
        Required input variables:
            GCWS Public Warrants
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
            GCWS Public Warrants
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
        Required input variables:
            GCWS Public Warrants
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
            GCWS Public Warrants
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
        Required input variables:
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

        #GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
        #TODO
        #connect signals and slots - gcws_rail_design_warning_time_adjacent_crossing
        # .valueChanged.connect(self.gcws_rail_design_warning_time_adjacent_crossing)
        
        #TODO includes pedestrian clearance
        #connect signals and slots - gcws_rail_design_warning_time_clearance_distance
        '''
        Connect input variable signals to gcws_rail_design_warning_time_clearance_distance method slot.
        Required input variables:
            comboBox_design_road_design_vehicle_type
            doubleSpinBox_design_measure_clearance_distance_pedestrian
            doubleSpinBox_design_measure_clearance_distance_vehicle 
        Related methods:
            None
        '''
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.gcws_rail_design_warning_time_clearance_distance)
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.gcws_rail_design_warning_time_clearance_distance)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.gcws_rail_design_warning_time_clearance_distance)
        
        #connect signals and slots - gcws_rail_design_warning_time_departure_time_vehicle
        '''
        Connect input variable signals to gcws_rail_design_warning_time_departure_time_vehicle method slot.
        Required input variables:
            doubleSpinBox_design_measure_clearance_distance_pedestrian
            doubleSpinBox_design_measure_clearance_distance_vehicle
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
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.gcws_rail_design_warning_time_departure_time_vehicle)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.gcws_rail_design_warning_time_departure_time_vehicle)
        self.view.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self.model.gcws_rail_design_warning_time_departure_time_vehicle)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.gcws_rail_design_warning_time_departure_time_vehicle)

        #connect signals and slots - gcws_rail_design_warning_time_departure_time_pedestrian
        '''
        Connect input variable signals to gcws_rail_design_warning_time_departure_time_pedestrian method slot.
        Required input variables:
            doubleSpinBox_design_measure_clearance_distance_pedestrian
        Related methods:
            self.model.design_calculate_clearance_time_pedestrian_design_check
        '''
        self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.gcws_rail_design_warning_time_departure_time_pedestrian)

        #connect signals and slots - gcws_rail_design_warning_time_gate_arm_clearance
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
        #TODO Remove Pedestrian clearance distance
        # self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self.model.gcws_rail_design_warning_time_gate_arm_clearance('doubleSpinBox_design_measure_clearance_distance_pedestrian', val))
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
        Required input variables:
            spinBox_general_info_road_speed_design
            doubleSpinBox_design_measure_clearance_distance_vehicle
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
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.gcws_rail_design_warning_time_ssd)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.gcws_rail_design_warning_time_ssd)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.gcws_rail_design_warning_time_ssd)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.gcws_rail_design_warning_time_ssd)

        #TODO
        # connect signals and slots - gcws_rail_design_approach_warning_time
        # .valueChanged.connect(self.gcws_rail_design_approach_warning_time)
        
        # GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
        
        #TODO
        #connect signals and slots - gates_gcws_calculate_inner_gate_arm_delay_time_recommended
        '''
        Connect input variable signals to gates_gcws_calculate_inner_gate_arm_delay_time_recommended method slot.
        Required input variables: 
            doubleSpinBox_design_measure_adjacent_track_separation_distance, doubleSpinBox_design_measure_adjacent_track_clearance_distance
        Related methods:
            None
        '''
        self.view.doubleSpinBox_design_measure_adjacent_track_separation_distance.valueChanged.connect(self.model.gates_gcws_calculate_inner_gate_arm_delay_time_recommended)
        self.view.doubleSpinBox_design_measure_adjacent_track_clearance_distance.valueChanged.connect(self.model.gates_gcws_calculate_inner_gate_arm_delay_time_recommended)

        # PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
        #TODO
        #connect signals and slots - aawd_calculate_advance_activation_time_design_n_or_e_approach
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
            design_calculate_vehicle_travel_distance
            design_lookup_design_vehicle_length
            aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended
            label_design_input_reaction_time
        '''
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.aawd_calculate_advance_activation_time_design_n_or_e_approach)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.aawd_calculate_advance_activation_time_design_n_or_e_approach)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.aawd_calculate_advance_activation_time_design_n_or_e_approach)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.aawd_calculate_advance_activation_time_design_n_or_e_approach)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.aawd_calculate_advance_activation_time_design_n_or_e_approach)
        
        #TODO
        #connect signals and slots - aawd_calculate_advance_activation_time_design_s_or_w_approach
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
            design_calculate_vehicle_travel_distance
            design_lookup_design_vehicle_length
            aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended
            label_design_input_reaction_time
        '''
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.aawd_calculate_advance_activation_time_design_s_or_w_approach)
        self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self.model.aawd_calculate_advance_activation_time_design_s_or_w_approach)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self.model.aawd_calculate_advance_activation_time_design_s_or_w_approach)
        self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self.model.aawd_calculate_advance_activation_time_design_s_or_w_approach)
        self.view.comboBox_design_road_design_vehicle_type.currentTextChanged.connect(self.model.aawd_calculate_advance_activation_time_design_s_or_w_approach)

        #TODO
        #connect signals and slots - aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended
        '''
        Connect input variable signals to aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended method slot.
        Required input variables:
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
        Required input variables:
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
        Required input variables:
            comboBox_general_info_road_classification
        Related methods:
            None
        '''
        self.view.comboBox_general_info_road_classification.currentTextChanged.connect(self.model.aawd_warrant_gcr_lookup_road_classification)

        #connect signals and slots - aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr
        '''
        Connect input variable signals to aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr method slot.
        required input variables:
            spinBox_general_info_road_speed_design
        required methods:
            None
        '''
        self.view.spinBox_general_info_road_speed_design.valueChanged.connect(self.model.aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr)
        
        # INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
        #connect signals and slots - preemption_of_traffic_signals_lookup_proximity_condition
        '''
        Connect input variable signals to preemption_of_traffic_signals_lookup_proximity_condition method slot.
        required input variables:
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach
            doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach
        required methods:
            None
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

        # WHISTLE CESSATION (GCS SECTION Appendix D)
        #TODO
        #connect signals and slots - areas_without_train_whistling_lookup_gcs_9_2
        '''
        Connect input variable signals to areas_without_train_whistling_lookup_gcs_9_2 method slot.
        required input variables:
            comboBox_gcws_observe_gates_n_or_e_approach
            comboBox_gcws_observe_gates_s_or_w_approach
            GCWS Public Warrants
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
            GCWS Public Warrants
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
        self.view.comboBox_gcws_observe_gates_n_or_e_approach.currentTextChanged.connect(self.model.areas_without_train_whistling_lookup_gcs_9_2)
        self.view.comboBox_gcws_observe_gates_s_or_w_approach.currentTextChanged.connect(self.model.areas_without_train_whistling_lookup_gcs_9_2)
        self.view.comboBox_general_info_road_sidewalks.currentTextChanged.connect(self.model.areas_without_train_whistling_lookup_gcs_9_2)
        self.view.comboBox_inspection_details_grade_crossing_type.currentTextChanged.connect(self.model.areas_without_train_whistling_lookup_gcs_9_2)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach.valueChanged.connect(self.model.areas_without_train_whistling_lookup_gcs_9_2)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_or_w_approach.valueChanged.connect(self.model.areas_without_train_whistling_lookup_gcs_9_2)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach.valueChanged.connect(self.model.areas_without_train_whistling_lookup_gcs_9_2)
        self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_or_w_approach.valueChanged.connect(self.model.areas_without_train_whistling_lookup_gcs_9_2)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.areas_without_train_whistling_lookup_gcs_9_2)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.areas_without_train_whistling_lookup_gcs_9_2)
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.areas_without_train_whistling_lookup_gcs_9_2)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.areas_without_train_whistling_lookup_gcs_9_2)
        self.view.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self.model.areas_without_train_whistling_lookup_gcs_9_2)
        self.view.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self.model.areas_without_train_whistling_lookup_gcs_9_2)
        self.view.spinBox_general_info_road_aadt_forecast.valueChanged.connect(self.model.areas_without_train_whistling_lookup_gcs_9_2)

        #connect signals and slots - areas_without_train_whistling_requirements_lookup_table_d1_criteria
        '''
        Connect input variable signals to areas_without_train_whistling_requirements_lookup_table_d1_criteria method slot.
        required input variables:
            spinBox_general_info_rail_no_tracks_main
            spinBox_general_info_rail_no_tracks_other
            spinBox_general_info_rail_max_railway_operating_speed_freight 
            spinBox_general_info_rail_max_railway_operating_speed_passenger
        required methods:
            general_info_rail_no_tracks_total
            general_info_rail_railway_design_speed
        '''
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.areas_without_train_whistling_requirements_lookup_table_d1_criteria)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.areas_without_train_whistling_requirements_lookup_table_d1_criteria)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.areas_without_train_whistling_requirements_lookup_table_d1_criteria)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.areas_without_train_whistling_requirements_lookup_table_d1_criteria)

        #connect signals and slots - areas_without_train_whistling_requirements_observe_table_d1
        '''
        Connect input variable signals to areas_without_train_whistling_requirements_observe_table_d1 method slot.
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
            areas_without_train_whistling_requirements_lookup_table_d1_criteria
            general_info_rail_no_tracks_total
            general_info_rail_railway_design_speed
        '''
        self.view.comboBox_gcws_observe_gates_n_or_e_approach.currentTextChanged.connect(self.model.areas_without_train_whistling_requirements_observe_table_D1)
        self.view.comboBox_gcws_observe_gates_s_or_w_approach.currentTextChanged.connect(self.model.areas_without_train_whistling_requirements_observe_table_D1)
        self.view.comboBox_gcws_observe_light_units_n_or_e_approach.currentTextChanged.connect(self.model.areas_without_train_whistling_requirements_observe_table_D1)
        self.view.comboBox_gcws_observe_light_units_s_or_w_approach.currentTextChanged.connect(self.model.areas_without_train_whistling_requirements_observe_table_D1)
        self.view.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self.model.areas_without_train_whistling_requirements_observe_table_D1)
        self.view.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self.model.areas_without_train_whistling_requirements_observe_table_D1)
        self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self.model.areas_without_train_whistling_requirements_observe_table_D1) 
        self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self.model.areas_without_train_whistling_requirements_observe_table_D1)

    '''DATABASE SAMPLE CODE START'''
    #Database Sample Code
    def get_id_for_row(self, index):
        index = index.siblingAtColumn(0)
        coffee_id = self.coffee_list.model().data(index)
        return coffee_id

    def show_coffee(self, coffee_id):
        # get the basic coffee information
        query1 = qts.QSqlQuery(self.db)
        query1.prepare('SELECT * FROM crossing_ca_inventory WHERE id=:id')
        query1.bindValue(':id', coffee_id)
        query1.exec()
        query1.next()
        coffee = {
            'id': query1.value(0),
            'coffee_brand': query1.value(1),
            'coffee_name': query1.value(2),
            'roast_id': query1.value(3)
        }
        # get the reviews
        query2 = qts.QSqlQuery()
        query2.prepare('SELECT * FROM reviews WHERE coffee_id=:id')
        query2.bindValue(':id', coffee_id)
        query2.exec()
        reviews = []
        while query2.next():
            reviews.append((
                query2.value('reviewer'),
                query2.value('review_date'),
                query2.value('review')
            ))

        self.coffee_form.show_coffee(coffee, reviews)
        self.stack.setCurrentWidget(self.coffee_form)
        '''DATABASE SAMPLE CODE END'''
        
