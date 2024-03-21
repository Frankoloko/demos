import { Component, Injectable, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-loading-icon',
  templateUrl: './loading-icon.html',
  styleUrls: ['./loading-icon.scss']
})

@Injectable()
export class LoadingIcon implements OnInit {
  @Input() imageSrc;
  @Input() loading;

  // HOW TO USE
    // <app-loading-icon [loading]="loadVariable" imageSrc="../../assets/insight-icon.svg"></app-loading-icon>

  turningForward = true;

  constructor() {}

  ngOnInit() {
    this.startRandomAnimation();
  }

  startRandomAnimation() {
    const randomDuration = (Math.floor(Math.random() * 3) + 1) * 1000;

    if (this.loading) {
      setTimeout(() => {
        this.turningForward = !this.turningForward;
        this.startRandomAnimation();
      }, randomDuration);
    }
  }
}
