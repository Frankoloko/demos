// SERVICE/SOURCE ##########################################################################
import { Subject } from 'rxjs/Subject';

TheSourceClient = new Subject();
constructor() {
    this.TheSourceClient.next('Francois');
};


// COMPONENT WHERE YOU DISPLAY THE VALUE (WHERE THE SUBSCRIPTION NEEDS TO BE MADE) ##########################################################################
import { SharedData } from '../../shared/shared.data';

private subscription : Subscription;

TheCurrentClient : string;
constructor(private SharedData: SharedData) {
    this.SharedData.TheSourceClient.subscribe((pClient) => {this.TheCurrentClient = pClient})
}


// COMPONENT WHERE THE VALUE WILL CHANGE ##########################################################################
import { SharedData } from '../../shared/shared.data';

constructor (private SharedData: SharedData) {}

this.SharedData.TheSourceClient.next('Phillip');